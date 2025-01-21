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

# 사용자별 반려동물 목록 조회
def view_my_pets(user_id):
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 로그인한 사용자 ID에 해당하는 반려동물 정보 가져오기
    cursor.execute("SELECT name, age, species, breed FROM pets WHERE family_id = ?", (user_id,))
    pets = cursor.fetchall()

    if pets:
        print("\n나의 반려동물 목록:")
        for pet in pets:
            print(f"이름: {pet[0]}, 나이: {pet[1]}, 종: {pet[2]}, 품종: {pet[3]}")
    else:
        print("\n등록된 반려동물이 없습니다.")

    conn.close()  # 데이터베이스 연결 종료

# 반려동물 수정 함수
def update_pet():
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

    pet_id = int(input("수정할 반려동물 ID를 입력하세요: "))
    name = input("새로운 이름 (Enter를 누르면 변경하지 않음): ")
    age = input("새로운 나이 (Enter를 누르면 변경하지 않음): ")
    species = input("새로운 종 (Enter를 누르면 변경하지 않음): ")
    breed = input("새로운 품종 (Enter를 누르면 변경하지 않음): ")

    updates = []
    params = []
    if name:
        updates.append("name = ?")
        params.append(name)
    if age:
        updates.append("age = ?")
        params.append(int(age))
    if species:
        updates.append("species = ?")
        params.append(species)
    if breed:
        updates.append("breed = ?")
        params.append(breed)

    if updates:
        params.append(pet_id)
        query = f"UPDATE pets SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(query, tuple(params))
        conn.commit()
        print("반려동물 정보가 성공적으로 수정되었습니다!")
    else:
        print("변경된 내용이 없습니다.")
    conn.close()

# 반려동물 삭제 함수
def delete_pet():
    conn = sqlite3.connect("withpaw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM pets")
    pets = cursor.fetchall()
    if not pets:
        print("등록된 반려동물이 없습니다.")
        conn.close()
        return

    print("\n반려동물 목록:")
    for pet in pets:
        print(f"ID: {pet[0]}, 이름: {pet[1]}")

    pet_id = int(input("삭제할 반려동물 ID를 입력하세요: "))
    confirm = input(f"정말로 반려동물(ID: {pet_id})을 삭제하시겠습니까? (y/n): ")
    if confirm.lower() == 'y':
        cursor.execute("DELETE FROM pets WHERE id = ?", (pet_id,))
        conn.commit()
        print("반려동물이 성공적으로 삭제되었습니다!")
    else:
        print("삭제가 취소되었습니다.")
    conn.close()