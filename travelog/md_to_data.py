#!/usr/bin/env python3
"""Day00~Day15.md → data.js 의 DAY_PLANS 배열로 변환"""
import re, json
from pathlib import Path

MD_DIR  = Path(__file__).parent.parent / "여행계획"
DATA_JS = Path(__file__).parent / "data.js"

# 날짜 매핑 (Day00 = 출발 전날 8/2, Day01~15 = 8/3~8/17)
DAY_DATES = {
    0:  ("2026-08-02", "8/2(일)", "출발 전날"),
    1:  ("2026-08-03", "8/3(월)", "서울→수원→춘천"),
    2:  ("2026-08-04", "8/4(화)", "춘천"),
    3:  ("2026-08-05", "8/5(수)", "춘천→강릉"),
    4:  ("2026-08-06", "8/6(목)", "강릉→경주"),
    5:  ("2026-08-07", "8/7(금)", "경주"),
    6:  ("2026-08-08", "8/8(토)", "경주→부산"),
    7:  ("2026-08-09", "8/9(일)", "부산"),
    8:  ("2026-08-10", "8/10(월)", "부산→통영"),
    9:  ("2026-08-11", "8/11(화)", "통영→하동→여수"),
    10: ("2026-08-12", "8/12(수)", "여수·금오도"),
    11: ("2026-08-13", "8/13(목)", "여수→지리산"),
    12: ("2026-08-14", "8/14(금)", "지리산→전주"),
    13: ("2026-08-15", "8/15(토)", "전주"),
    14: ("2026-08-16", "8/16(일)", "전주→충주→단양"),
    15: ("2026-08-17", "8/17(월)", "단양→서울"),
}

def extract_key_items(md: str) -> list[str]:
    """시간표 테이블에서 핵심 일정 최대 5개 추출"""
    items = []
    for line in md.splitlines():
        m = re.match(r'\|\s*(\d{2}:\d{2})\s*\|\s*\*{0,2}(.+?)\*{0,2}\s*\|', line)
        if m:
            time, place = m.group(1), m.group(2).strip()
            place = re.sub(r'\*+', '', place).strip()
            if place and place not in ('장소', '시간', '—', '-'):
                items.append(f"{time} {place}")
    return items[:5]

def extract_desc(md: str) -> str:
    """첫 번째 blockquote(> …) 또는 첫 비어있지 않은 일반 문단"""
    for line in md.splitlines():
        line = line.strip()
        if line.startswith('>') and not line.startswith('> ⚠️') and not line.startswith('> 💡'):
            return line.lstrip('> ').strip()
    return ""

def parse_md(day_num: int) -> dict:
    path = MD_DIR / f"Day{day_num:02d}.md"
    if not path.exists():
        return None
    md = path.read_text(encoding='utf-8')

    # H1 타이틀
    m = re.search(r'^#\s+(.+)', md, re.MULTILINE)
    title = m.group(1).strip() if m else f"Day {day_num:02d}"
    # 이모지 제거
    title = re.sub(r'[🗺️🌊🏯🌅🏖️🚣🪂🪨🍱🎨🌿🏕️🎆🍜🍙🧄]', '', title).strip()

    date_str, date_label, route = DAY_DATES.get(day_num, ("", "", ""))

    return {
        "dayNum":    day_num,
        "date":      date_str,
        "dateLabel": date_label,
        "route":     route,
        "title":     title,
        "desc":      extract_desc(md),
        "keyItems":  extract_key_items(md),
        "content":   md,
    }

plans = []
for i in range(16):  # Day00 ~ Day15
    p = parse_md(i)
    if p:
        plans.append(p)

print(f"✅ {len(plans)}개 Day 파일 파싱 완료")

# data.js 업데이트: DAY_PLANS 블록 교체 또는 삽입
js = DATA_JS.read_text(encoding='utf-8')
plans_js = "const DAY_PLANS = " + json.dumps(plans, ensure_ascii=False, indent=2) + ";\n"

if "const DAY_PLANS" in js:
    js = re.sub(r'const DAY_PLANS\s*=[\s\S]*?;\n', plans_js, js)
else:
    js = js.rstrip() + "\n\n" + plans_js

DATA_JS.write_text(js, encoding='utf-8')
print(f"✅ data.js DAY_PLANS 업데이트 완료 ({len(plans)}개)")
