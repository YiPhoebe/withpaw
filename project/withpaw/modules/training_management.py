import sqlite3

def initialize_training_table():
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 훈련 기록 테이블 생성 (존재하지 않으면)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS training_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pet_id INTEGER NOT NULL,
        training_date TEXT NOT NULL,
        training_type TEXT NOT NULL,
        duration INTEGER NOT NULL,
        notes TEXT,
        FOREIGN KEY (pet_id) REFERENCES pets (id)
    )
    ''')

    conn.commit()
    conn.close()

def add_training_record(pet_id):
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    training_date = input("훈련 날짜를 입력하세요 (YYYY-MM-DD): ")
    training_type = input("훈련 유형을 입력하세요 (예: 산책, 복종 훈련 등): ")
    try:
        duration = int(input("훈련 시간을 입력하세요 (분 단위): "))
    except ValueError:
        print("훈련 시간은 숫자로 입력해야 합니다.")
        conn.close()
        return

    notes = input("훈련 메모를 입력하세요 (선택 사항): ")

    cursor.execute('''
    INSERT INTO training_records (pet_id, training_date, training_type, duration, notes)
    VALUES (?, ?, ?, ?, ?)
    ''', (pet_id, training_date, training_type, duration, notes))

    conn.commit()
    conn.close()
    print("훈련 기록이 성공적으로 추가되었습니다!")

def view_training_records(pet_id):
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    cursor.execute('''
    SELECT training_date, training_type, duration, notes
    FROM training_records
    WHERE pet_id = ?
    ORDER BY training_date DESC
    ''', (pet_id,))

    records = cursor.fetchall()

    if records:
        print("\n훈련 기록:")
        for record in records:
            date, t_type, duration, notes = record
            print(f"날짜: {date}, 유형: {t_type}, 시간: {duration}분, 메모: {notes or '없음'}")
    else:
        print("훈련 기록이 없습니다.")

    conn.close()

def delete_training_record(record_id):
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    cursor.execute("DELETE FROM training_records WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()
    print("훈련 기록이 삭제되었습니다.")

def view_and_delete_training_record(pet_id):
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    cursor.execute('''
    SELECT id, training_date, training_type, duration, notes
    FROM training_records
    WHERE pet_id = ?
    ORDER BY training_date DESC
    ''', (pet_id,))

    records = cursor.fetchall()

    if not records:
        print("훈련 기록이 없습니다.")
        conn.close()
        return

    print("\n삭제 가능한 훈련 기록:")
    for record in records:
        r_id, date, t_type, duration, notes = record
        print(f"ID: {r_id}, 날짜: {date}, 유형: {t_type}, 시간: {duration}분, 메모: {notes or '없음'}")

    try:
        record_id = int(input("삭제할 기록의 ID를 입력하세요: "))
        delete_training_record(record_id)
    except ValueError:
        print("유효한 숫자를 입력하세요.")

    conn.close()

if __name__ == "__main__":
    initialize_training_table()
    while True:
        print("\n[훈련 기록 관리]")
        print("1. 훈련 기록 추가")
        print("2. 훈련 기록 보기")
        print("3. 훈련 기록 삭제")
        print("4. 종료")

        choice = input("선택: ")

        if choice == "1":
            try:
                pet_id = int(input("훈련 기록을 추가할 반려동물 ID를 입력하세요: "))
                add_training_record(pet_id)
            except ValueError:
                print("유효한 숫자를 입력하세요.")
        elif choice == "2":
            try:
                pet_id = int(input("훈련 기록을 볼 반려동물 ID를 입력하세요: "))
                view_training_records(pet_id)
            except ValueError:
                print("유효한 숫자를 입력하세요.")
        elif choice == "3":
            try:
                pet_id = int(input("삭제할 기록이 있는 반려동물 ID를 입력하세요: "))
                view_and_delete_training_record(pet_id)
            except ValueError:
                print("유효한 숫자를 입력하세요.")
        elif choice == "4":
            print("훈련 기록 관리를 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
