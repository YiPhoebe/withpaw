import sqlite3  # SQLite3 모듈을 가져옵니다.

# 데이터베이스 초기화 함수
def initialize_database():
    conn = sqlite3.connect('withpaw.db')  # 데이터베이스 파일 연결 (없으면 생성됨)
    cursor = conn.cursor()  # 커서 객체 생성

    # 사용자 프로필 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_profile (
        id INTEGER PRIMARY KEY,              -- 사용자 ID (사용자가 직접 입력)
        username TEXT NOT NULL UNIQUE,       -- 사용자 아이디 (고유값)
        password TEXT NOT NULL,              -- 사용자 비밀번호
        name TEXT,                           -- 사용자 이름
        email TEXT                           -- 사용자 이메일 (선택)
    )
    """)  # user_profile 테이블 생성

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
    """)  # pets 테이블 생성

    # 훈련 기록 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS training_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 훈련 기록 ID (자동 증가)
        pet_id INTEGER,                        -- 반려동물 ID (pets와 연결)
        date TEXT NOT NULL,                    -- 훈련 날짜
        description TEXT NOT NULL,             -- 훈련 기록 설명
        FOREIGN KEY(pet_id) REFERENCES pets(id)  -- 외래 키 설정
    )
    """)  # training_records 테이블 생성

    conn.commit()  # 변경 사항 저장
    conn.close()   # 데이터베이스 연결 종료
    print("데이터베이스와 테이블이 성공적으로 생성되었습니다!")  # 성공 메시지 출력

# 데이터베이스 초기화 함수 (테이블 삭제 후 재생성)
def reset_database():
    conn = sqlite3.connect('withpaw.db')  # 데이터베이스 파일 연결
    cursor = conn.cursor()  # 커서 객체 생성

    # 기존 테이블 삭제
    cursor.execute("DROP TABLE IF EXISTS training_records")  # training_records 테이블 삭제
    cursor.execute("DROP TABLE IF EXISTS pets")  # pets 테이블 삭제
    cursor.execute("DROP TABLE IF EXISTS user_profile")  # user_profile 테이블 삭제

    # 데이터베이스 재초기화
    initialize_database()  # 초기화 함수 호출

    print("데이터베이스가 성공적으로 초기화되었습니다!")  # 성공 메시지 출력
    conn.close()  # 데이터베이스 연결 종료
