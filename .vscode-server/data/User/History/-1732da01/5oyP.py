import sqlite3

# 반려동물 등록 함수
def add_pet():
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 사용자 목록 출력
    cursor.execute("SELECT id, name FROM user_profile")
    users = cursor.fetchall()
    if not users:  # 등록된 사용자가 없을 경우
        print("등록된 사용자가 없습니다. 먼저 사용자 프로필을 생성해주세요.")  # 경고 메시지
        conn.close()
        return

    print("\n사용자 목록:")
    for user in users:
        print(f"ID: {user[0]}, 이름: {user[1]}")

    # 반려동물 가족 ID 입력 받기
    family_id = int(input("반려동물의 가족 ID를 입력하세요: "))
    name = input("반려동물 이름을 입력하세요: ")
    age = int(input("반려동물 나이를 입력하세요: "))
    species = input("반려동물 종을 입력하세요 (예: 강아지, 고양이): ")
    breed = input("반려동물 품종을 입력하세요: ")

    # 반려동물 정보 삽입
    cursor.execute("""
    INSERT INTO pets (name, age, species, breed, family_id)
    VALUES (?, ?, ?, ?, ?)
    """, (name, age, species, breed, family_id))
    conn.commit()  # 변경 사항 저장
    conn.close()   # 데이터베이스 연결 종료
    print(f"반려동물 {name}이(가) 성공적으로 등록되었습니다!")  # 성공 메시지

# 반려동물 정보 수정 함수
def update_pet():
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 반려동물 목록 출력
    cursor.execute("SELECT id, name FROM pets")
    pets = cursor.fetchall()
    if not pets:  # 등록된 반려동물이 없을 경우
        print("등록된 반려동물이 없습니다. 먼저 반려동물을 등록해주세요.")  # 경고 메시지
        conn.close()
        return

    print("\n반려동물 목록:")
    for pet in pets:
        print(f"ID: {pet[0]}, 이름: {pet[1]}")

    # 수정할 반려동물 선택
    pet_id = int(input("수정할 반려동물의 ID를 입력하세요: "))
    name = input("새 이름 (현재 이름 유지하려면 Enter): ")
    age = input("새 나이 (현재 나이 유지하려면 Enter): ")

    # 업데이트 쿼리 작성
    updates = []
    params = []
    if name:
        updates.append("name = ?")
        params.append(name)
    if age:
        updates.append("age = ?")
        params.append(int(age))
    updates_query = ", ".join(updates)
    query = f"UPDATE pets SET {updates_query} WHERE id = ?"
    params.append(pet_id)

    # 반려동물 정보 수정
    cursor.execute(query, tuple(params))
    conn.commit()  # 변경 사항 저장
    conn.close()   # 데이터베이스 연결 종료
    print("반려동물 정보가 성공적으로 수정되었습니다!")  # 성공 메시지