from database import initialize_database, reset_database
from user_management import set_user_profile, login
from pet_management import add_pet

if __name__ == "__main__":
    initialize_database()  # 데이터베이스 초기화
    while True:
        print("\n1. 사용자 프로필 생성")
        print("2. 로그인")
        print("3. 반려동물 등록")
        print("4. 종료")
        choice = input("선택: ")
        if choice == "1":
            set_user_profile()
        elif choice == "2":
            login()
        elif choice == "3":
            add_pet()
        elif choice == "4":
            print("WithPaw를 종료합니다. 감사합니다!")
            break
        else:
            print("잘못된 입력입니다. 다시 시도해주세요!")