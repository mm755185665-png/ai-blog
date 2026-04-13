#!/usr/bin/env python3
"""
批量将 tools-zh 的 markdown 文件翻译为英文，输出到 tools-en
"""
import json
import re
import time
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import quote

ZH_DIR = Path(__file__).parent.parent / "src" / "content" / "tools-zh"
EN_DIR = Path(__file__).parent.parent / "src" / "content" / "tools-en"

# 分类名中英映射
CATEGORY_MAP = {
    "AI编程工具": "AI Coding Tools",
    "AI大模型":   "AI Models",
    "AI写作工具": "AI Writing Tools",
    "AI图像生成": "AI Image Generation",
    "AI视频工具": "AI Video Tools",
    "AI效率工具": "AI Productivity Tools",
    "AI音频工具": "AI Audio Tools",
}

# tag 中英映射
TAG_MAP = {
    "免费":     "Free",
    "付费":     "Paid",
    "免费/付费": "Free/Paid",
}


def translate(text: str) -> str:
    """Google Translate 免费接口，中文 → 英文"""
    if not text or not text.strip():
        return text
    try:
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=zh-CN&tl=en&dt=t&q={quote(text)}"
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        result = "".join(seg[0] for seg in data[0] if seg[0])
        # 替换双引号，避免破坏 YAML 格式
        result = result.replace('"', "'").strip()
        return result or text
    except Exception as e:
        print(f"    [翻译失败] {e}")
        return text


def translate_list_field(yaml_text: str, field: str) -> str:
    """翻译 YAML 列表字段（features/pros/cons）"""
    pattern = rf'^({field}:\s*\n)((?:  - ".+"\n?)+)'
    def replace_list(m):
        header = m.group(1)
        items_block = m.group(2)
        items = re.findall(r'  - "(.+?)"', items_block)
        translated = []
        for item in items:
            t = translate(item)
            time.sleep(0.2)
            translated.append(f'  - "{t}"')
        return header + "\n".join(translated) + "\n"
    return re.sub(pattern, replace_list, yaml_text, flags=re.MULTILINE)


def process_file(zh_path: Path) -> None:
    en_path = EN_DIR / zh_path.name
    if en_path.exists():
        print(f"  [SKIP] {zh_path.name} (已存在)")
        return

    content = zh_path.read_text(encoding="utf-8")

    # 解析 frontmatter
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not m:
        print(f"  [SKIP] {zh_path.name} (无 frontmatter)")
        return

    fm, body = m.group(1), m.group(2)

    # 翻译 category
    for zh, en in CATEGORY_MAP.items():
        fm = fm.replace(f'category: {zh}', f'category: {en}')

    # 翻译 tag
    tag_m = re.search(r'^tag: (.+)$', fm, re.MULTILINE)
    if tag_m:
        zh_tag = tag_m.group(1).strip()
        en_tag = TAG_MAP.get(zh_tag, zh_tag)
        fm = fm.replace(f'tag: {zh_tag}', f'tag: {en_tag}')

    # 翻译 longDesc
    ld_m = re.search(r'^longDesc: "(.+?)"$', fm, re.MULTILINE | re.DOTALL)
    if ld_m:
        translated_ld = translate(ld_m.group(1))
        time.sleep(0.3)
        fm = fm.replace(ld_m.group(0), f'longDesc: "{translated_ld}"')

    # 翻译 pricing
    pr_m = re.search(r'^pricing: "(.+?)"$', fm, re.MULTILINE | re.DOTALL)
    if pr_m:
        translated_pr = translate(pr_m.group(1))
        time.sleep(0.3)
        fm = fm.replace(pr_m.group(0), f'pricing: "{translated_pr}"')

    # 翻译列表字段
    for field in ("features", "pros", "cons"):
        fm = translate_list_field(fm, field)

    # 翻译正文
    translated_body = ""
    if body.strip():
        translated_body = translate(body.strip())
        time.sleep(0.3)

    result = f"---\n{fm}\n---\n\n{translated_body}\n"
    EN_DIR.mkdir(parents=True, exist_ok=True)
    en_path.write_text(result, encoding="utf-8")
    print(f"  [OK] {zh_path.name}")


def main():
    files = sorted(ZH_DIR.glob("*.md"))
    print(f"共 {len(files)} 个工具文件，开始翻译...\n")
    for i, f in enumerate(files, 1):
        print(f"[{i}/{len(files)}] {f.name}")
        process_file(f)
    print(f"\n完成！英文文件已保存到 {EN_DIR}")


if __name__ == "__main__":
    main()
