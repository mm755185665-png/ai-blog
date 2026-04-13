#!/usr/bin/env python3
"""
每日 AI 资讯抓取脚本
从多个 RSS 源抓取最新 AI 资讯，输出到 src/data/news.json
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError
import xml.etree.ElementTree as ET

OUTPUT = Path(__file__).parent.parent / "src" / "data" / "news.json"
MAX_PER_FEED = 20
MAX_TOTAL = 100

FEEDS = [
    {"name": "量子位",   "url": "https://www.qbitai.com/feed"},
    {"name": "机器之心", "url": "https://www.jiqizhixin.com/rss"},
    {"name": "少数派",   "url": "https://sspai.com/feed"},
    {"name": "36Kr",    "url": "https://36kr.com/feed"},
    {"name": "爱范儿",  "url": "https://www.ifanr.com/feed"},
]

NS = {
    "atom":    "http://www.w3.org/2005/Atom",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc":      "http://purl.org/dc/elements/1.1/",
}


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_date(text: str) -> datetime:
    """Parse various RSS date formats → UTC datetime."""
    if not text:
        return datetime.now(timezone.utc)
    # RFC 822: "Mon, 13 Apr 2026 08:00:00 +0800"
    fmts = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S GMT",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%d",
    ]
    text = text.strip()
    for fmt in fmts:
        try:
            dt = datetime.strptime(text, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except ValueError:
            continue
    return datetime.now(timezone.utc)


def fetch_feed(name: str, url: str) -> list[dict]:
    """Fetch and parse one RSS/Atom feed. Returns list of item dicts."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; news-bot/1.0)"}
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=15) as resp:
            raw = resp.read()
    except URLError as e:
        print(f"  [SKIP] {name}: {e}", file=sys.stderr)
        return []

    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        print(f"  [SKIP] {name}: XML parse error: {e}", file=sys.stderr)
        return []

    items = []

    # --- RSS 2.0 ---
    for item in root.findall(".//item")[:MAX_PER_FEED]:
        title = (item.findtext("title") or "").strip()
        link  = (item.findtext("link")  or "").strip()
        desc  = strip_html(item.findtext("description") or "")
        pub   = item.findtext("pubDate") or item.findtext("dc:date", namespaces=NS) or ""
        if not title or not link:
            continue
        items.append({
            "title":   title,
            "url":     link,
            "source":  name,
            "summary": desc[:200] + ("…" if len(desc) > 200 else ""),
            "date":    parse_date(pub).strftime("%Y-%m-%d"),
            "_ts":     parse_date(pub).timestamp(),
        })

    # --- Atom ---
    if not items:
        for entry in root.findall("atom:entry", NS)[:MAX_PER_FEED]:
            title = (entry.findtext("atom:title", namespaces=NS) or "").strip()
            link_el = entry.find("atom:link", NS)
            link  = (link_el.get("href") if link_el is not None else "") or ""
            summary_el = entry.find("atom:summary", NS) or entry.find("atom:content", NS)
            desc  = strip_html(summary_el.text if summary_el is not None else "")
            pub   = entry.findtext("atom:published", namespaces=NS) or \
                    entry.findtext("atom:updated", namespaces=NS) or ""
            if not title or not link:
                continue
            items.append({
                "title":   title,
                "url":     link,
                "source":  name,
                "summary": desc[:200] + ("…" if len(desc) > 200 else ""),
                "date":    parse_date(pub).strftime("%Y-%m-%d"),
                "_ts":     parse_date(pub).timestamp(),
            })

    print(f"  [OK] {name}: {len(items)} items")
    return items


def main():
    all_items: list[dict] = []
    for feed in FEEDS:
        all_items.extend(fetch_feed(feed["name"], feed["url"]))

    # Deduplicate by URL
    seen: set[str] = set()
    unique = []
    for item in all_items:
        if item["url"] not in seen:
            seen.add(item["url"])
            unique.append(item)

    # Sort newest first
    unique.sort(key=lambda x: x["_ts"], reverse=True)
    unique = unique[:MAX_TOTAL]

    # Remove internal sort key
    for item in unique:
        del item["_ts"]

    output = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "items":   unique,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nDone: {len(unique)} items → {OUTPUT}")


if __name__ == "__main__":
    main()
