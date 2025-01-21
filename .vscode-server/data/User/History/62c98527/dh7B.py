import sqlite3

def initialize_database():
    conn = sqlite3.connect("withpaw.db")
    cursor = conn.cursor()

    # 사용자 테이블
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        name TEXT,
        email TEXT
    )
    """)

    # 반려동물 테이블
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        species TEXT,
        breed TEXT,
        family_id INTEGER,
        FOREIGN KEY(family_id) REFERENCES user_profile(id)
    )
    """)

    # 반려동물 공유 테이블
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS shared_pets (
        pet_id INTEGER,
        shared_with_user_id INTEGER,
        PRIMARY KEY (pet_id, shared_with_user_id),
        FOREIGN KEY(pet_id) REFERENCES pets(id),
        FOREIGN KEY(shared_with_user_id) REFERENCES user_profile(id)
    )
    """)

    # 훈련 기록 테이블
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS training_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pet_id INTEGER,
        training TEXT NOT NULL,
        success BOOLEAN NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY(pet_id) REFERENCES pets(id)
    )
    """)

    print("데이터베이스 및 테이블 생성 완료!")
    conn.commit()
    conn.close()

def reset_database():
    conn = sqlite3.connect("withpaw.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS user_profile")
    cursor.execute("DROP TABLE IF EXISTS pets")
    cursor.execute("DROP TABLE IF EXISTS shared_pets")
    cursor.execute("DROP TABLE IF EXISTS training_records")
    initialize_database()
    print("데이터베이스 리셋 완료!")
    conn.close()