from database import initialize_database    # 데이터베이스 초기화 관련 함수를 가져옴
from user_management import set_user_profile, login     # 사용자 관리 관련 함수 (프로플 생성 및 로그인)를 가져옴
from pet_management import add_pet, update_pet, delete_pet, view_my_pets    # 반려동물 관리 관련 함수 (등록, 수정, 삭제, 조회)를 가져옴
from training_management import add_training_record, view_training_records  # 훈련 기록 관리 함수 (추가 및 조회)를 가져옴

def main_menu():    # 메인 메뉴를 출력
    print("\n1. 사용자 프로필 생성")
    print("2, 로그인")
    print("3. 종료")

def family_menu():  # 나의 가족 보기 메뉴를 출력
    print("\n[나의 가족 보기]]")    
    print("1. 반려동물 등록")
    print("2. 반려동물 정보 수정")
    print("3. 반려동물 정보 삭제")
    print("4. 나의 반려동물 보기")
    print("5. 뒤로 가기")

def training_menu():    # 훈련 기록을 출력
    print("\n[훈련 기록]")
    print("1. 훈련 기록 추가")
    print("2. 훈련 기록 보기")
    print("3. 뒤로 가기")

def execute_family_choice(choice, logged_in_user):  # 나의 가족 보기 메뉴에서 선택된 옵션을 실행하는 함수의 정의
    match choice:   # 선택된 옵션에 따라 실행할 작업을 결정
        case "1":
            add_pet()   # 실행
        case "2":
            update_pet()
        case "3":
            delete_pet()
        case "4":
            view_my_pets(logged_in_user[0])
        case "5":
            return False    # 뒤로가기 선택 시 False 반환
        case _:     # 잘못된 입력 처리
            print("잘못된 입력입니다. 다시 시도해주세요.")
    return True

def execute_training_choice(choice, logged_in_user):    # 훈련 기록 메뉴에서 선택된 옵션을 실행하는 함수의 정의
    match choice:
        case "1":
            add_training_record(logged_in_user[0])
        case "2":
            view_training_records(logged_in_user[0])
        case "3":
            return False
        case _:
            print("잘못된 입력입니다. 다시 시도해주세요.")
    return True

def main():     # 프로그램의 진입점으로, main 루트 실행하는 함수
    initialize_database()   # 데이터베이스 초기화 실행

    logged_in_user = None   # 로그인 상태 저장

    while True:     # 사용자와의 상호작용을 계속해서 처리하기 위한 무한 루프
        if not logged_in_user:  # 로그인 상태가 아닌 경우 메인 메뉴를 표시함
            main_menu()     # 메인 메뉴 출력
            choice = input("선택: ")

            match choice:   # 선택된 옵션에 따라 실행할 작엽 결정
                case "1":
                    set_user_profile()
                case "2":
                    logged_in_user = login()
                case "3":
                    print("WithPaw를 종료합니다. 감사합니다!")
                case _:
                    print("잘못된 입력입니다. 다시 시도해주세요.")
        else:   # 로그인 상태인 경우
            print("\n안녕하세요, {logged_in_user[3]}님!")
            print("1. 나의 가족 보기")
            print("2. 훈련 기록")
            print("3. 로그아웃")
            print("4. 종료")

            choice = input("선택: ")

            match choice:
                case "1":
                    while True:
                        family_menu()
                        family_choice = input("선택: ")

                        if not execute_family_choice(family_choice, logged_in_user):
                            break   # 뒤로 가기 시 루프 종료

                case "2":
                    while True:
                        training_menu()
                        training_choice = input("선택: ")

                        if not execute_training_choice(training_choice, logged_in_user):
                            break

                case "3":
                    print("로그아웃 되었습니다.")
                    logged_in_user = None
                
                case "4":
                    print("WithPaw를 종료합니다. 감사합니다!")
                    break

                case _:
                    print("잘못된 입력입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()