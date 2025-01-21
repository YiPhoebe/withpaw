import sqlite3

# 반려동물 등록 함수
def add_pet():
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 사용자 목록 출력
    cursor.execute("SELECT id, name FROM user_profile")
    users = cursor.fetchall()
    if not users:  # 등록된 사용자가 없을 경우
        print("등록된 사용자가 없습니다. 먼저 사용자 프로필을 생성해주세요.")
        conn.close()
        return

    print("\n사용자 목록:")
    for user in users:
        print(f"ID: {user[0]}, 이름: {user[1]}")

    family_id = int(input("반려동물의 가족 ID를 입력하세요: "))
    name = input("반려동물 이름을 입력하세요: ")
    age = int(input("반려동물 나이를 입력하세요: "))
    species = input("반려동물 종을 입력하세요 (예: 강아지, 고양이): ")
    breed = input("반려동물 품종을 입력하세요: ")

    cursor.execute("""
    INSERT INTO pets (name, age, species, breed, family_id)
    VALUES (?, ?, ?, ?, ?)
    """, (name, age, species, breed, family_id))

    conn.commit()  # 변경 사항 저장
    conn.close()   # 데이터베이스 연결 종료
    print(f"반려동물 {name}이(가) 성공적으로 등록되었습니다!")

# 반려동물 목록 보기 함수
def view_my_pets(user_id):
    conn = sqlite3.connect("withpaw.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, age, species, breed FROM pets WHERE family_id = ?", (user_id,))
    pets = cursor.fetchall()

    if pets:
        print("\n나의 반려동물 목록:")
        for pet in pets:
            print(f"이름: {pet[0]}, 나이: {pet[1]}, 종: {pet[2]}, 품종: {pet[3]}")
    else:
        print("등록된 반려동물이 없습니다.")
    conn.close()