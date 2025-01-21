import sqlite3
from datetime import datetime

# 훈련 기록 테이블 초기화 함수
def initialize_training_table():
    conn = sqlite3.connect("withpaw.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS training_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pet_id INTEGER NOT NULL,
        description TEXT,
        date TEXT,
        success INTEGER,
        FOREIGN KEY(pet_id) REFERENCES pets(id)
    )
    """)

    conn.commit()
    conn.close()
    print("훈련 기록 테이블이 성공적으로 생성되었습니다!")

# 날짜 유효성 검사 함수
def get_valid_date():
    while True:
        date_input = input("훈련 날짜를 입력하세요 (예: YYYY-MM-DD): ")
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("유효하지 않은 날짜 형식입니다. 다시 입력해주세요.")

def add_training_record(user_id):  # 사용자 ID를 매개변수로 받음
    import sqlite3  # SQLite3 모듈을 가져옴

    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 사용자별 반려동물 목록 가져오기
    cursor.execute("SELECT id, name FROM pets WHERE family_id = ?", (user_id,))
    pets = cursor.fetchall()

    if not pets:
        print("등록된 반려동물이 없습니다. 먼저 반려동물을 등록해주세요.")
        conn.close()
        return

    print("\n훈련 기록을 추가할 반려동물을 선택하세요:")
    for pet in pets:
        print(f"ID: {pet[0]}, 이름: {pet[1]}")

    # 반려동물 ID 입력 받기
    pet_id = int(input("반려동물 ID를 입력하세요: "))
    description = input("훈련 기록을 입력하세요: ")  # 훈련 기록 설명 입력
    date = input("훈련 날짜를 입력하세요 (예: 2025-01-01): ")  # 날짜 입력

    # 훈련 기록 데이터 삽입
    cursor.execute("""
    INSERT INTO training_records (pet_id, date, description)
    VALUES (?, ?, ?)
    """, (pet_id, date, description))
    conn.commit()  # 변경 사항 저장
    conn.close()   # 데이터베이스 연결 종료

    print("훈련 기록이 성공적으로 추가되었습니다!")

# 훈련 성공 여부 입력 함수
def get_training_success():
    while True:
        success = input("훈련 성공 여부를 입력하세요 (y/n): ").lower()
        if success in ('y', 'n'):
            return success == 'y'
        else:
            print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")

# 훈련 기록 보기 함수
def view_training_records(user_id):
    conn = sqlite3.connect("withpaw.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT pets.name, training_records.description, training_records.date, training_records.success
    FROM training_records
    JOIN pets ON training_records.pet_id = pets.id
    WHERE pets.family_id = ?
    """, (user_id,))
    records = cursor.fetchall()

    if records:
        print("\n훈련 기록 목록:")
        for record in records:
            status = "성공" if record[3] == 1 else "실패"
            print(f"반려동물 이름: {record[0]}, 훈련 내용: {record[1]}, 날짜: {record[2]}, 결과: {status}")
    else:
        print("\n훈련 기록이 없습니다.")
    
    conn.close()