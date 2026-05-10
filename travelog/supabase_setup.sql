-- ══════════════════════════════════════════════════
-- Supabase SQL Editor에 이 내용을 붙여넣고 실행하세요
-- ══════════════════════════════════════════════════

-- 1. 게시물 테이블
CREATE TABLE IF NOT EXISTS posts (
  id            UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  created_at    TIMESTAMPTZ DEFAULT NOW(),
  trip_date     DATE NOT NULL,
  day_number    INTEGER,
  location_name TEXT NOT NULL,
  region        TEXT,
  lat           FLOAT,
  lng           FLOAT,
  content       TEXT,
  photo_urls    TEXT[] DEFAULT '{}',
  weather       TEXT
);

-- 2. 누구나 읽기/쓰기 가능 (개인 여행 블로그용)
ALTER TABLE posts ENABLE ROW LEVEL SECURITY;
CREATE POLICY "read_all"   ON posts FOR SELECT USING (true);
CREATE POLICY "insert_all" ON posts FOR INSERT WITH CHECK (true);
CREATE POLICY "update_all" ON posts FOR UPDATE USING (true);
CREATE POLICY "delete_all" ON posts FOR DELETE USING (true);

-- 3. 사진 저장소(버킷) 생성
INSERT INTO storage.buckets (id, name, public)
VALUES ('travel-photos', 'travel-photos', true)
ON CONFLICT DO NOTHING;

-- 4. 저장소 접근 정책
CREATE POLICY "upload_all" ON storage.objects
  FOR INSERT WITH CHECK (bucket_id = 'travel-photos');
CREATE POLICY "view_all"   ON storage.objects
  FOR SELECT USING (bucket_id = 'travel-photos');
CREATE POLICY "delete_own" ON storage.objects
  FOR DELETE USING (bucket_id = 'travel-photos');
