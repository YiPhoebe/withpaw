from database import initialize_database  # 데이터베이스 초기화 관련 함수를 가져옵니다.
from user_management import set_user_profile, login, find_username, find_password  # 사용자 관리 관련 함수 (프로필 생성, 로그인, 아이디/비밀번호 찾기)를 가져옵니다.
from pet_management import add_pet, update_pet, delete_pet, update_pet_notes, view_my_pets  # 반려동물 관리 관련 함수 (등록, 수정, 삭제, 조회)를 가져옵니다.
from training_management import add_training_record, view_training_records  # 훈련 기록 관리 함수 (추가 및 조회)를 가져옵니다.

def main_menu():  # 메인 메뉴를 출력하는 함수의 정의입니다.
    print("\n1. 사용자 프로필 생성")
    print("2. 로그인")
    print("3. 종료")

def family_menu():  # 나의 가족 보기 메뉴를 출력하는 함수의 정의입니다.
    print("\n[나의 가족 보기]")  # 나의 가족 보기 메뉴 제목 출력
    print("1. 반려동물 정보 등록")  # 반려동물 등록 옵션 출력
    print("2. 반려동물 정보 수정")  # 반려동물 수정 옵션 출력
    print("3. 반려동물 정보 삭제")  # 반려동물 삭제 옵션 출력
    print("4. 나의 반려동물 보기")  # 나의 반려동물 보기 옵션 출력
    print("5. 반려동물 특성 추가")
    print("6. 뒤로 가기")  # 뒤로 가기 옵션 출력

def training_menu():  # 훈련 기록 메뉴를 출력하는 함수의 정의입니다.
    print("\n[훈련 기록]")  # 훈련 기록 메뉴 제목 출력
    print("1. 훈련 기록 추가")  # 훈련 기록 추가 옵션 출력
    print("2. 훈련 기록 보기")  # 훈련 기록 보기 옵션 출력
    print("3. 뒤로 가기")  # 뒤로 가기 옵션 출력

def execute_family_choice(choice, logged_in_user):  # 나의 가족 보기 메뉴에서 선택된 옵션을 실행하는 함수의 정의입니다.
    match choice:  # 선택된 옵션에 따라 실행할 작업을 결정합니다.
        case "1":
            add_pet()  # 반려동물 등록 실행
        case "2":
            update_pet()  # 반려동물 수정 실행
        case "3":
            delete_pet()  # 반려동물 삭제 실행
        case "4":
            view_my_pets(logged_in_user[0])  # 나의 반려동물 보기 실행
        case "5":
            update_pet_notes()
        case "6":
            return False  # 뒤로 가기 선택 시 False 반환
        case _:
            print("잘못된 입력입니다. 다시 시도해주세요!")  # 잘못된 입력 처리
    return True  # 계속 실행 상태 반환

def execute_training_choice(choice, logged_in_user):  # 훈련 기록 메뉴에서 선택된 옵션을 실행하는 함수의 정의입니다.
    match choice:  # 선택된 옵션에 따라 실행할 작업을 결정합니다.
        case "1":
            add_training_record(logged_in_user[0])  # 훈련 기록 추가 실행
        case "2":
            view_training_records(logged_in_user[0])  # 훈련 기록 보기 실행
        case "3":
            return False  # 뒤로 가기 선택 시 False 반환
        case _:
            print("잘못된 입력입니다. 다시 시도해주세요!")  # 잘못된 입력 처리
    return True  # 계속 실행 상태 반환

def main():  # 프로그램의 진입점으로, main 루프를 실행하는 함수의 정의입니다.
    initialize_database()  # 데이터베이스 초기화 실행

    logged_in_user = None  # 로그인 상태 저장

    while True:  # 사용자와의 상호작용을 계속해서 처리하기 위한 무한 루프
        if not logged_in_user:  # 로그인 상태가 아닌 경우 메인 메뉴를 표시합니다.
            main_menu()  # 메인 메뉴 출력
            choice = input("선택: ")  # 사용자 입력 받기

            match choice:  # 선택된 옵션에 따라 실행할 작업을 결정합니다.
                case "1":
                    set_user_profile()  # 사용자 프로필 생성 실행
                case "2":
                    logged_in_user = login()  # 사용자 로그인 실행
                    if not logged_in_user:  # 로그인 실패 시
                        print("로그인에 실패했습니다. 아이디나 비밀번호를 확인해주세요.")
                        print("1. 아이디 찾기")
                        print("2. 비밀번호 찾기")
                        recovery_choice = input("선택: ")
                        match recovery_choice:
                            case "1":
                                find_username()  # 아이디 찾기 실행
                            case "2":
                                find_password()  # 비밀번호 찾기 실행
                            case _:
                                print("잘못된 입력입니다. 메인 메뉴로 돌아갑니다.")
                case "3":
                    print("WithPaw를 종료합니다. 감사합니다!")  # 종료 메시지 출력
                    break  # 프로그램 종료
                case _:
                    print("잘못된 입력입니다. 다시 시도해주세요!")  # 잘못된 입력 처리
        else:  # 로그인 상태인 경우
            print(f"\n안녕하세요, {logged_in_user[3]}님!")  # 환영 메시지 출력
            print("1. 나의 가족 보기")  # 나의 가족 보기 옵션 출력
            print("2. 훈련 기록")  # 훈련 기록 옵션 출력
            print("3. 로그아웃")  # 로그아웃 옵션 출력
            print("4. 종료")  # 종료 옵션 출력

            choice = input("선택: ")  # 사용자 입력 받기

            match choice:  # 선택된 옵션에 따라 실행할 작업을 결정합니다.
                case "1":
                    while True:  # 나의 가족 보기 메뉴 루프 실행
                        family_menu()  # 나의 가족 보기 메뉴 출력
                        family_choice = input("선택: ")  # 사용자 입력 받기

                        if not execute_family_choice(family_choice, logged_in_user):  # 나의 가족 보기 메뉴 처리
                            break  # 뒤로 가기 시 루프 종료

                case "2":
                    while True:  # 훈련 기록 메뉴 루프 실행
                        training_menu()  # 훈련 기록 메뉴 출력
                        training_choice = input("선택: ")  # 사용자 입력 받기

                        if not execute_training_choice(training_choice, logged_in_user):  # 훈련 기록 메뉴 처리
                            break  # 뒤로 가기 시 루프 종료

                case "3":
                    print("로그아웃 되었습니다.")  # 로그아웃 메시지 출력
                    logged_in_user = None  # 로그인 상태 초기화

                case "4":
                    print("WithPaw를 종료합니다. 감사합니다!")  # 종료 메시지 출력
                    break  # 프로그램 종료

                case _:
                    print("잘못된 입력입니다. 다시 시도해주세요!")  # 잘못된 입력 처리

if __name__ == "__main__":
    main()  # main 함수 실행
