from database import initialize_database
from user_management import set_user_profile, login
from pet_management import add_pet, view_my_pets

if __name__ == "__main__":
    initialize_database()  # 데이터베이스 초기화

    logged_in_user = None  # 로그인 상태를 저장하는 변수

    while True:
        # 로그인 상태에 따라 메뉴를 다르게 표시
        if logged_in_user:
            print(f"\n안녕하세요, {logged_in_user[3]}님!")
            print("1. 반려동물 등록")
            print("2. 나의 반려동물 목록 보기")
            print("3. 로그아웃")
            print("4. 종료")
        else:
            print("\n1. 사용자 프로필 생성")
            print("2. 로그인")
            print("3. 종료")

        # 사용자 선택
        choice = input("선택: ")

        # 로그인 상태에 따라 동작 분기
        if not logged_in_user:
            if choice == "1":
                set_user_profile()
            elif choice == "2":
                logged_in_user = login()
            elif choice == "3":
                print("WithPaw를 종료합니다. 감사합니다!")
                break
            else:
                print("잘못된 입력입니다. 다시 시도해주세요!")
        else:
            if choice == "1":
                add_pet()
            elif choice == "2":
                view_my_pets(logged_in_user[0])  # 로그인한 사용자의 ID 전달
            elif choice == "3":
                print("로그아웃 되었습니다.")
                logged_in_user = None  # 로그인 상태 초기화
            elif choice == "4":
                print("WithPaw를 종료합니다. 감사합니다!")
                break
            else:
                print("잘못된 입력입니다. 다시 시도해주세요!")