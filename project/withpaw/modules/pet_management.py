import sys
import os
import sqlite3

# 필요한 모듈 경로를 추가
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

# 데이터베이스 초기화 함수
def initialize_database():
    conn = sqlite3.connect("withpaw.db")
    cursor = conn.cursor()

    # 테이블 생성 (존재하지 않으면)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT, -- 자동 증가
        name TEXT NOT NULL,
        age INTEGER,
        species TEXT,
        breed TEXT,
        notes TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        display_name TEXT
    )
    ''')

    conn.commit()
    conn.close()

# 사용자 관리 함수들
from user_management import set_user_profile, login, find_username, find_password

# 반려동물 관리 함수들
def add_pet():
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    name = input("반려동물 이름을 입력하세요: ")
    try:
        age = int(input("반려동물 나이를 입력하세요: "))
    except ValueError:
        print("유효한 숫자를 입력하세요.")
        conn.close()
        return

    species = input("반려동물 종을 입력하세요 (예: 강아지, 고양이): ")
    breed = input("반려동물 품종을 입력하세요: ")

    # 데이터베이스에 반려동물 정보 추가 (id는 자동 생성)
    cursor.execute(
        "INSERT INTO pets (name, age, species, breed) VALUES (?, ?, ?, ?)",
        (name, age, species, breed),
    )
    conn.commit()
    conn.close()

    print(f"반려동물 {name}이(가) 성공적으로 등록되었습니다!")

def view_my_pets(user_id):
    conn = sqlite3.connect("withpaw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, species, breed, notes FROM pets")
    pets = cursor.fetchall()
    conn.close()
    return pets

def update_pet(pet_id, new_data):
    conn = sqlite3.connect("withpaw.db")
    cursor = conn.cursor()

    fields = ["name", "age", "species", "breed", "notes"]
    updates = []
    values = []

    for field in fields:
        if field in new_data:
            updates.append(f"{field} = ?")
            values.append(new_data[field])

    if updates:
        values.append(pet_id)
        query = f"UPDATE pets SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(query, values)
        conn.commit()
        print("반려동물 정보가 수정되었습니다.")
    else:
        print("변경 사항이 없습니다.")

    conn.close()

def delete_pet(pet_id):
    conn = sqlite3.connect("withpaw.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pets WHERE id = ?", (pet_id,))
    conn.commit()
    conn.close()
    print("반려동물이 삭제되었습니다.")

# 메인 메뉴
if __name__ == "__main__":
    initialize_database()

    while True:
        print("\n[WithPaw 관리 시스템]")
        print("1. 사용자 프로필 설정")
        print("2. 로그인")
        print("3. 종료")
        choice = input("선택: ")

        if choice == "1":
            set_user_profile()
        elif choice == "2":
            user = login()
            if user:
                print(f"\n{user['display_name']}님 환영합니다!")
                while True:
                    print("\n1. 반려동물 등록")
                    print("3. 반려동물 정보 수정")
                    print("4. 반려동물 정보 삭제")
                    print("5. 로그아웃")
                    user_choice = input("선택: ")

                    if user_choice == "1":
                        add_pet()
                    elif user_choice == "2":
                        pets = view_my_pets(user['id'])
                        for pet in pets:
                            print(f"이름: {pet[0]}, 나이: {pet[1]}, 종: {pet[2]}, 품종: {pet[3]}, 메모: {pet[4]}")
                    elif user_choice == "3":
                        pet_id = int(input("수정할 반려동물 ID: "))
                        new_data = {
                            "name": input("새 이름 (없으면 Enter): ") or None,
                            "age": input("새 나이 (없으면 Enter): ") or None,
                            "species": input("새 종 (없으면 Enter): ") or None,
                            "breed": input("새 품종 (없으면 Enter): ") or None,
                            "notes": input("새 메모 (없으면 Enter): ") or None,
                        }
                        update_pet(pet_id, {k: v for k, v in new_data.items() if v})
                    elif user_choice == "4":
                        pet_id = int(input("삭제할 반려동물 ID: "))
                        delete_pet(pet_id)
                    elif user_choice == "5":
                        print("로그아웃되었습니다.")
                        break
                    else:
                        print("잘못된 입력입니다.")
            else:
                print("로그인 실패.")
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")
