# 2026 국토대장정 여행 플래너

아버지와 아들(중1)의 21일 국토종주 여행 기록 프로젝트.  
2026년 8월 3일 ~ 8월 23일 | 서울 → 파주 → 강원 → 경북 → 부산 → 전남(여수·지리산) → 전주 → 충주 → 서울

🌐 **배포 사이트**: Netlify (GitHub 연동, 자동 배포)

---

## 프로젝트 구조

```
2026-Cross-Country/
├── 2026_국토대장정_여행플래너.xlsx   # 마스터 데이터 (일정·맛집·예약)
├── CLAUDE.md                         # AI 작업 원칙
├── README.md
├── .github/workflows/
│   └── excel-sync.yml                # Excel → data.js 자동 변환 Actions
└── travelog/
    ├── index.html                    # 메인 앱 (단일 파일 SPA)
    ├── data.js                       # 자동 생성 데이터 (직접 수정 금지)
    ├── config.js                     # Supabase 설정
    ├── excel_to_data.py              # Excel → data.js 변환 스크립트
    └── supabase_setup.sql            # Supabase DB 초기화 SQL
```

---

## 앱 기능

| 탭 | 내용 |
|---|---|
| 🗺️ 지도 | 기록된 글 위치 핀 표시, 클릭 시 기록 탭 이동 |
| 📋 일정 | 21일 일정표, 날짜별 접기/펼치기, 예약 상태 연동 |
| 🍽️ 맛집 | 42개 지역 맛집, 지역·종류 이중 필터 |
| 🎫 예약 | 27개 예약 항목 관리, 완료 체크, 예약 링크 |
| 📖 기록 | 여행 중 사진·글 피드 (Supabase 연동) |
| ✏️ 새 글 | 비밀번호 인증 후 글·사진 업로드 |

---

## 데이터 수정 워크플로우

> ⚠️ `travelog/data.js`는 자동 생성 파일입니다. **직접 수정 금지**.

### Excel 수정 → 로컬 검증 → xlsx 푸시

```bash
# 1. Excel 수정 후 루트 디렉토리에서 data.js 로컬 검증
cd travelog
python3 excel_to_data.py
# ✅ data.js 생성: 7개 권역, 42개 맛집, 27개 예약 출력 확인

# 2. 로컬 브라우저 확인 (선택)
python3 -m http.server 8080
# → http://localhost:8080/index.html

# 3. xlsx만 커밋·푸시
cd ..
git add 2026_국토대장정_여행플래너.xlsx
git commit -m "Excel 업데이트: (수정 내용 요약)"
git push origin main
# → GitHub Actions가 data.js 자동 재생성
# → Netlify 자동 배포
```

**Excel만 수정하면 되는 경우**
- 일정 내용 변경
- 맛집 추가/수정
- 예약 항목 추가/수정

**index.html 직접 수정이 필요한 경우**
- UI/디자인 변경
- 새 탭·기능 추가
- 버그 수정

---

## index.html 또는 스크립트 수정 후 푸시

```bash
# 변경된 파일만 선택해서 커밋
git add travelog/index.html travelog/excel_to_data.py
git commit -m "기능 수정: (수정 내용)"
git push origin main
```

---

## 날짜 변경 시 수정 위치

여행 날짜가 바뀌면 두 곳을 수정해야 합니다.

```bash
# 1. travelog/index.html (617~618번 줄)
const START = new Date(2026, 7, 3);   // 월은 0-indexed: 7 = 8월
const END   = new Date(2026, 7, 23);

# 2. travelog/excel_to_data.py (115번 줄)
_START = _date(2026, 8, 3)            # 예약 Day 번호 계산 기준
```

---

## 기술 스택

- **프론트엔드**: 순수 HTML/CSS/JS (단일 파일, 프레임워크 없음)
- **지도**: Leaflet.js
- **백엔드**: Supabase (글·사진 저장)
- **호스팅**: Netlify (정적 배포, 크레딧 소비 없음)
- **자동화**: GitHub Actions (Excel → data.js 변환)

---

## 초기 설정

### 1. Supabase 설정
`travelog/config.js`에 Supabase URL과 키 입력.  
DB 구조는 `travelog/supabase_setup.sql` 참고.

### 2. 로컬 실행
```bash
cd travelog && python3 -m http.server 8080
# → http://localhost:8080/index.html
```

### 3. GitHub Actions 권한
저장소 Settings → Actions → General → Workflow permissions → **Read and write** 설정 필요.

---

## 보안

- `travelog/Security-information.md` — GitHub PAT 보관 (`.gitignore` 처리됨)
- 글쓰기 비밀번호: `config.js`의 `adminPassword` 값
