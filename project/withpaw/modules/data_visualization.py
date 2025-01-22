import sqlite3  # 데이터베이스 연결

# 데이터베이스 초기화 함수

def initialize_database():
    conn = sqlite3.connect("Withpaw.db")    # 데이터베이스 파일 연결
    cursor = conn.cursor()

    # user_profile 테이블 생성
    cursor.execute(
        """
        CREATE TABLE IF NOT EXIST user_profile (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            name TEXT NOT NULL
        )
        """
    )

    # pats 테이블 생성
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NLL,
            age INTEGER,
            secies TEXT,
            bread TEXT,
            owner_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES user_profile (id)
        )
        """
    )

    conn.commit()   # 변경 사항 저장
    conn.close()    # 데이터베이스 연결 종료

    print("데이터 베이스와 테이블이 성공적으로 생성되었습니다.")