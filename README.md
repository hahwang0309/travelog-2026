# 🗺 부자 국토대장정 여행 플래너

아버지와 아들(중1)의 21일 국토종주 여행 기록 프로젝트.  
순수 HTML/CSS/JS 단일 파일 SPA — 프레임워크·빌드 없음.

**[데모 보기 →](https://hahwang0309.github.io/travelog-2026/travelog/)**

---

## ✨ 앱 기능

| 탭 | 내용 |
|---|---|
| 🗺️ 지도 | 기록된 글 위치 핀 표시, 클릭 시 기록 탭 이동 |
| 📋 일정 | 날짜별 접기/펼치기, PDF 다운로드 |
| 🍽️ 맛집 | 지역·종류 이중 필터 |
| 🎫 예약 | 예약 항목 완료 체크, 예약 링크 |
| 📖 기록 | 여행 중 사진·글 피드 (Supabase 연동) |
| ✏️ 새 글 | 비밀번호 인증 후 글·사진 업로드 |

---

## 🚀 나만의 여행 플래너로 포크해서 사용하기

### 1단계 — 저장소 포크 & GitHub Pages 활성화

1. 이 저장소 우측 상단 **Fork** 버튼 클릭
2. 포크된 내 저장소 → **Settings** → **Pages**
3. Source: `Deploy from a branch` → Branch: `main` / Folder: `/ (root)` → **Save**
4. 잠시 후 `https://<your-username>.github.io/<repo-name>/travelog/` 에서 접속 가능

> GitHub Actions 자동 변환 기능을 쓰려면  
> Settings → Actions → General → Workflow permissions → **Read and write** 허용

---

### 2단계 — 여행 데이터 수정

모든 여행 데이터는 **Excel 파일 하나**로 관리됩니다.

```
2026_국토대장정_여행플래너.xlsx
├── DAY_PLANS 시트  — 날짜별 일정
├── RESTAURANTS 시트 — 맛집 목록
└── RESERVATIONS 시트 — 예약 항목
```

Excel 수정 후 `xlsx` 파일만 커밋·푸시하면 GitHub Actions가 `data.js`를 자동 재생성합니다.

```bash
git add 2026_국토대장정_여행플래너.xlsx
git commit -m "여행 일정 업데이트"
git push origin main
# → Actions 자동 실행 → data.js 재생성 → GitHub Pages 반영
```

로컬에서 미리 확인하려면:

```bash
cd travelog
python3 excel_to_data.py   # data.js 재생성
python3 -m http.server 8080
# → http://localhost:8080/index.html
```

---

### 3단계 — 날짜·제목 수정

여행 기간이 다르면 두 곳을 수정합니다.

**`travelog/index.html`** (약 617번 줄)
```js
const START = new Date(2026, 7, 3);   // 월은 0-indexed: 7 = 8월
const END   = new Date(2026, 7, 23);
```

**`travelog/excel_to_data.py`** (약 115번 줄)
```python
_START = _date(2026, 8, 3)   # 예약 Day 번호 계산 기준
```

---

### 4단계 — 사진·글 기록 기능 설정 (선택)

기록 탭(사진·글 업로드)은 [Supabase](https://supabase.com) 를 사용합니다.  
이 기능이 필요 없으면 이 단계는 건너뛰어도 됩니다.

1. [supabase.com](https://supabase.com) 에서 새 프로젝트 생성
2. `travelog/supabase_setup.sql` 내용을 Supabase SQL Editor에서 실행
3. Storage에 `travel-photos` 버킷 생성 (Public)
4. **`travelog/config.js`** 수정:

```js
const SUPABASE_URL  = 'https://your-project.supabase.co';
const SUPABASE_KEY  = 'your-anon-key';
const adminPassword = 'your-password';   // 글쓰기 잠금 비밀번호
```

---

## 📁 프로젝트 구조

```
travelog-2026/
├── 2026_국토대장정_여행플래너.xlsx   # 마스터 데이터 (여기만 수정)
├── .github/workflows/
│   └── excel-sync.yml                # Excel → data.js 자동 변환 Actions
└── travelog/
    ├── index.html                    # 앱 전체 (HTML + CSS + JS 단일 파일)
    ├── data.js                       # 자동 생성 — 직접 수정 금지
    ├── config.js                     # Supabase 설정 (gitignore 권장)
    ├── excel_to_data.py              # Excel → data.js 변환 스크립트
    └── supabase_setup.sql            # DB 스키마
```

---

## 🛠 기술 스택

- **프론트엔드**: 순수 HTML/CSS/JS (프레임워크·빌드 없음)
- **지도**: Leaflet.js + OpenStreetMap
- **백엔드**: Supabase (글·사진 저장, 선택)
- **호스팅**: GitHub Pages (무료 정적 배포)
- **자동화**: GitHub Actions (Excel 변경 시 data.js 재생성)

---

## ⚠️ 주의사항

- `travelog/data.js` 는 자동 생성 파일 — **직접 수정 금지**
- `travelog/config.js` 에 Supabase 키를 넣을 경우 public 저장소라면 anon key만 사용 (RLS 설정 권장)
- GitHub Actions 첫 실행 시 Workflow permissions → Read and write 권한 필요
