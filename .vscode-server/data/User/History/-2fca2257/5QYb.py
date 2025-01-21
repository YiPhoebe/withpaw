from database import initialize_database
from user_management import set_user_profile, login
from pet_management import add_pet, view_my_pets

if __name__ == "__main__":
    initialize_database()  # 데이터베이스 초기화

    logged_in_user = None

    while True:
        print("\n1. 사용자 프로필 생성")
        print("2. 로그인")
        print("3. 반려동물 등록")
        print("4. 나의 반려동물 목록 보기")
        print("5. 종료")
        choice = input("선택: ")

        if choice == "1":
            set_user_profile()
        elif choice == "2":
            logged_in_user = login()
        elif choice == "3":
            if logged_in_user:
                add_pet()
            else:
                print("먼저 로그인하세요!")
        elif choice == "4":
            if logged_in_user:
                view_my_pets(logged_in_user[0])  # 로그인한 사용자의 ID 전달
            else:
                print("먼저 로그인하세요!")
        elif choice == "5":
            print("WithPaw를 종료합니다. 감사합니다!")
            break
        else:
            print("잘못된 입력입니다. 다시 시도해주세요!")