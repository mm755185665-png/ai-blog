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
MAX_PER_FEED = 30
MAX_TOTAL = 100

# 量子位/机器之心 是纯 AI 媒体，不过滤
# 少数派/36Kr/爱范儿 是综合科技媒体，需要关键词过滤
FEEDS = [
    # 国内 AI 媒体（纯 AI，不过滤）
    {"name": "量子位",   "url": "https://www.qbitai.com/feed",                              "ai_only": False},
    {"name": "机器之心", "url": "https://www.jiqizhixin.com/rss",                           "ai_only": False},
    {"name": "极客公园", "url": "https://www.geekpark.net/rss",                             "ai_only": False},
    {"name": "新智元",   "url": "https://xinzhiyuan.com/feed",                              "ai_only": False},
    # 国内综合科技媒体（需过滤 AI 相关）
    {"name": "少数派",   "url": "https://sspai.com/feed",                                   "ai_only": True},
    {"name": "36Kr",    "url": "https://36kr.com/feed",                                    "ai_only": True},
    {"name": "爱范儿",  "url": "https://www.ifanr.com/feed",                               "ai_only": True},
    {"name": "虎嗅",    "url": "https://www.huxiu.com/rss/0.xml",                          "ai_only": True},
    {"name": "钛媒体",  "url": "https://www.tmtpost.com/rss.xml",                          "ai_only": True},
    {"name": "IT之家",  "url": "https://www.ithome.com/rss/",                              "ai_only": True},
    # 国际 AI 媒体（英文，需过滤）
    {"name": "TechCrunch AI", "url": "https://techcrunch.com/category/artificial-intelligence/feed/", "ai_only": False},
    {"name": "The Verge AI",  "url": "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml", "ai_only": False},
    {"name": "VentureBeat AI","url": "https://venturebeat.com/category/ai/feed/",          "ai_only": False},
    {"name": "MIT Tech Review","url": "https://www.technologyreview.com/topic/artificial-intelligence/feed", "ai_only": False},
    # 官方博客（纯 AI，不过滤）
    {"name": "Google AI",     "url": "https://blog.research.google/feeds/posts/default",   "ai_only": True},
    {"name": "Hugging Face",  "url": "https://huggingface.co/blog/feed.xml",               "ai_only": False},
]

# AI 相关关键词（命中任意一个即保留）
AI_KEYWORDS = [
    "AI", "人工智能", "大模型", "ChatGPT", "GPT", "Claude", "Gemini",
    "DeepSeek", "Kimi", "豆包", "通义", "文心", "讯飞", "智谱",
    "机器学习", "深度学习", "神经网络", "LLM", "Agent", "多模态",
    "Sora", "Midjourney", "Stable Diffusion", "DALL", "文生图",
    "自动驾驶", "具身智能", "向量", "推理", "生成式", "OpenAI",
    "Anthropic", "Google DeepMind", "Meta AI", "Mistral",
    "Cursor", "Copilot", "代码助手", "AI助手", "AI工具",
]

def is_ai_related(title: str, summary: str) -> bool:
    text = (title + " " + summary).lower()
    return any(kw.lower() in text for kw in AI_KEYWORDS)

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
    except Exception as e:
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
        raw = fetch_feed(feed["name"], feed["url"])
        if feed.get("ai_only"):
            before = len(raw)
            raw = [i for i in raw if is_ai_related(i["title"], i["summary"])]
            print(f"       → AI过滤后: {len(raw)}/{before} items")
        all_items.extend(raw)

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
