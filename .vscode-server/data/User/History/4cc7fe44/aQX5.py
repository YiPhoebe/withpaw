import sqlite3

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

# 훈련 기록 추가 함수
def add_training_record():
    conn = sqlite3.connect("withpaw.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM pets")
    pets = cursor.fetchall()
    if not pets:
        print("등록된 반려동물이 없습니다. 먼저 반려동물을 등록해주세요.")
        conn.close()
        return

    print("\n반려동물 목록:")
    for pet in pets:
        print(f"ID: {pet[0]}, 이름: {pet[1]}")

    pet_id = int(input("훈련 기록을 추가할 반려동물의 ID를 입력하세요: "))
    description = input("훈련 내용을 입력하세요: ")
    date = input("훈련 날짜를 입력하세요 (예: YYYY-MM-DD): ")
    success = get_training_success()

    cursor.execute("""
    INSERT INTO training_records (pet_id, description, date, success)
    VALUES (?, ?, ?, ?)
    """, (pet_id, description, date, int(success)))

    conn.commit()
    conn.close()
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