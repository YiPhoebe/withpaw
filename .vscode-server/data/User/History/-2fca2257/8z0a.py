from database import initialize_database
from user_management import set_user_profile, login
from pet_management import add_pet, update_pet, delete_pet, view_my_pets, add_training_record

if __name__ == "__main__":
    initialize_database()  # 데이터베이스 초기화

    logged_in_user = None  # 로그인 상태 저장

    while True:
        if logged_in_user:
            print(f"\n안녕하세요, {logged_in_user[3]}님!")
            print("1. 반려동물 등록")
            print("2. 반려동물 수정")
            print("3. 반려동물 삭제")
            print("4. 나의 반려동물 보기")  # 나의 반려동물 보기 추가
            print("5. 훈련 기록 추가")  # 훈련 기록 추가
            print("6. 로그아웃")
            print("7. 종료")
        else:
            print("\n1. 사용자 프로필 생성")
            print("2. 로그인")
            print("3. 종료")

        choice = input("선택: ")

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
                add_pet()  # 반려동물 등록
            elif choice == "2":
                update_pet()  # 반려동물 수정
            elif choice == "3":
                delete_pet()  # 반려동물 삭제
            elif choice == "4":
                view_my_pets(logged_in_user[0])  # 나의 반려동물 보기 (사용자 ID 전달)
            elif choice == "5":
                add_training_record()  # 훈련 기록 추가
            elif choice == "6":
                print("로그아웃 되었습니다.")
                logged_in_user = None  # 로그인 상태 초기화
            elif choice == "7":
                print("WithPaw를 종료합니다. 감사합니다!")
                break
            else:
                print("잘못된 입력입니다. 다시 시도해주세요!")
