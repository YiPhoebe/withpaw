import sqlite3

# 데이터베이스 초기화 함수
def initialize_database():
    conn = sqlite3.connect('withpaw.db')  # 데이터베이스 파일 연결
    cursor = conn.cursor()

    # 사용자 프로필 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_profile (
        id INTEGER PRIMARY KEY,              -- 사용자 ID (사용자가 직접 입력)
        username TEXT NOT NULL UNIQUE,       -- 사용자 아이디 (고유값)
        password TEXT NOT NULL,              -- 사용자 비밀번호
        name TEXT,                           -- 사용자 이름
        email TEXT                           -- 사용자 이메일 (선택)
    )
    """)

    # 반려동물 정보 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 반려동물 ID (자동 증가)
        name TEXT NOT NULL,                    -- 반려동물 이름
        age INTEGER,                           -- 반려동물 나이
        species TEXT,                          -- 반려동물 종 (예: 강아지, 고양이)
        breed TEXT,                            -- 반려동물 품종
        family_id INTEGER,                     -- 반려동물 가족 ID (user_profile와 연결)
        FOREIGN KEY(family_id) REFERENCES user_profile(id)  -- 외래 키 설정
    )
    """)

    # 훈련 기록 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS training_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,   -- 훈련 기록 ID (자동 증가)
        pet_id INTEGER NOT NULL,               -- 반려동물 ID (외래 키)
        description TEXT,                      -- 훈련 설명
        date TEXT,                             -- 훈련 날짜
        success INTEGER,                       -- 훈련 성공 여부 (1: 성공, 0: 실패)
        FOREIGN KEY(pet_id) REFERENCES pets(id)  -- 외래 키 설정
    )
    """)

    conn.commit()  # 변경 사항 저장
    conn.close()   # 데이터베이스 연결 종료
    print("데이터베이스와 테이블이 성공적으로 생성되었습니다!")

# 데이터베이스 초기화 함수 (테이블 삭제 후 재생성)
def reset_database():
    conn = sqlite3.connect('withpaw.db')  # 데이터베이스 파일 연결
    cursor = conn.cursor()

    # 기존 테이블 삭제
    cursor.execute("DROP TABLE IF EXISTS user_profile")
    cursor.execute("DROP TABLE IF EXISTS pets")
    cursor.execute("DROP TABLE IF EXISTS training_records")

    # 데이터베이스 재초기화
    initialize_database()
    print("데이터베이스가 성공적으로 초기화되었습니다!")  # 메시지 한글화

    conn.close()  # 데이터베이스 연결 종료