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

    try:
        pet_id = int(input("훈련 기록을 추가할 반려동물의 ID를 입력하세요: "))
        if not any(pet[0] == pet_id for pet in pets):
            print("유효하지 않은 반려동물 ID입니다. 다시 시도해주세요.")
            conn.close()
            return
    except ValueError:
        print("숫자를 입력해주세요.")
        conn.close()
        return

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