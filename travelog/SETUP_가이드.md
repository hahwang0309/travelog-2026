# 🗺️ 트레블로그 셋업 가이드
## 총 소요 시간: 약 15분 / 비용: 무료

---

## STEP 1 — Supabase 계정 만들기 (5분)

1. **https://supabase.com** 접속 → `Start your project` 클릭
2. GitHub 또는 이메일로 가입
3. `New project` 클릭
   - Organization: 기본값
   - Name: `travelog-2026` (아무 이름이나 가능)
   - Database Password: 기억하기 쉬운 비밀번호 입력
   - Region: **Northeast Asia (Seoul)** 선택
4. `Create new project` → 약 1~2분 대기

---

## STEP 2 — 데이터베이스 & 저장소 설정 (3분)

1. 프로젝트 생성 완료 후 왼쪽 메뉴 **SQL Editor** 클릭
2. `New query` 클릭
3. `supabase_setup.sql` 파일 내용 전체 복사 → 붙여넣기
4. `RUN` 버튼 클릭 → `Success` 메시지 확인

---

## STEP 3 — API 키 복사 (2분)

1. 왼쪽 메뉴 **Project Settings** (⚙️ 아이콘) → **API** 클릭
2. 아래 두 값을 복사해두기:
   - **Project URL** → `https://pdahbhchgtrgbjqxsdwl.supabase.co/`
   - **anon / public** 키 → `sb_publishable_vy8dkhTz0jdPz0kUyBx7BA_p2Wrh_I6`

---

## STEP 4 — config.js 수정 (1분)

`travelog` 폴더 안의 **config.js** 파일을 열어서:

```js
const CONFIG = {
  supabaseUrl:   'https://xxxxxxxxxx.supabase.co',  // ← Project URL 붙여넣기
  supabaseKey:   'eyJhbGci...',                      // ← anon 키 붙여넣기
  adminPassword: 'jangjeong2026',                    // ← 원하는 비밀번호로 변경
};
```

저장 후 닫기.

---

## STEP 5 — Netlify에 배포 (3분)

1. **https://netlify.com** 접속 → 이메일로 무료 가입
2. 로그인 후 대시보드에서 **"Deploy manually"** 또는 **"Sites"** 탭으로 이동
3. `travelog` 폴더를 **통째로** 드래그해서 화면에 놓기
4. 잠시 후 주소 자동 생성: `https://랜덤이름.netlify.app`
5. 원하면 `Site settings > Domain management`에서 주소 변경 가능

---

## 완료! 사용 방법

### 여행 중 기록하기
1. 스마트폰 브라우저로 Netlify 주소 접속
2. **✏️ 새 글** 탭 → 비밀번호 입력
3. 날짜·날씨·권역·장소 선택 후 이야기 입력
4. 📸 탭해서 사진 선택 (여러 장 가능)
5. **📮 기록 저장하기** 클릭

### 지도 보기
- 🗺️ 지도 탭: 방문한 곳마다 초록색 핀 표시, 탭하면 사진과 내용 팝업

### 기록 보기
- 📖 기록 탭: 날짜순 카드 피드, 사진 탭하면 크게 보기

---

## 문제가 생기면?

| 증상 | 해결 |
|------|------|
| 저장이 안 돼요 | config.js URL/키 확인, Supabase SQL 재실행 |
| 사진이 안 올라가요 | storage 버킷 정책 확인 (SQL 다시 실행) |
| 지도가 안 나와요 | 인터넷 연결 확인 |
| 비밀번호가 안 먹혀요 | config.js adminPassword 확인 |
