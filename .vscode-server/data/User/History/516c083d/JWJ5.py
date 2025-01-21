from database import initialize_database  # 데이터베이스 초기화 함수
from user_management import set_user_profile, login, find_username, find_password  # 사용자 관리 관련 함수
from pet_management import add_pet, update_pet, delete_pet, update_pet_notes, view_my_pets  # 반려동물 관리 함수
from training_management import add_training_record, view_training_records  # 훈련 기록 관리 함수
from data_visualization import visualize_pet_statistics, visualize_training_statistics  # 데이터 시각화 함수 가져오기

def statistics_menu():  # 통계 및 데이터 시각화 메뉴
    print("\n[데이터 시각화 및 통계]")
    print("1. 반려동물 통계 보기")
    print("2. 훈련 기록 통계 보기")
    print("3. 뒤로 가기")

def execute_statistics_choice(choice):  # 통계 메뉴 선택 실행 함수
    match choice:
        case "1":
            visualize_pet_statistics()  # 반려동물 통계 보기 실행
        case "2":
            visualize_training_statistics()  # 훈련 기록 통계 보기 실행
        case "3":
            return False  # 뒤로 가기
        case _:
            print("잘못된 입력입니다. 다시 시도해주세요!")
    return True

def main():  # 메인 함수
    initialize_database()  # 데이터베이스 초기화

    logged_in_user = None  # 로그인 상태 저장

    while True:
        if not logged_in_user:
            print("\n1. 사용자 프로필 생성")
            print("2. 로그인")
            print("3. 아이디 찾기")
            print("4. 비밀번호 찾기")
            print("5. 종료")
            choice = input("선택: ")

            match choice:
                case "1":
                    set_user_profile()
                case "2":
                    logged_in_user = login()
                case "3":
                    find_username()
                case "4":
                    find_password()
                case "5":
                    print("WithPaw를 종료합니다. 감사합니다!")
                    break
                case _:
                    print("잘못된 입력입니다. 다시 시도해주세요!")
        else:
            print(f"\n안녕하세요, {logged_in_user[3]}님!")
            print("1. 나의 가족 보기")
            print("2. 훈련 기록")
            print("3. 데이터 시각화 및 통계")
            print("4. 로그아웃")
            print("5. 종료")
            choice = input("선택: ")

            match choice:
                case "1":
                    while True:
                        print("\n[나의 가족 보기]")
                        print("1. 반려동물 정보 등록")
                        print("2. 반려동물 정보 수정")
                        print("3. 반려동물 정보 삭제")
                        print("4. 나의 반려동물 보기")
                        print("5. 반려동물 특성 추가")
                        print("6. 뒤로 가기")
                        family_choice = input("선택: ")
                        if family_choice == "6":
                            break
                        execute_family_choice(family_choice, logged_in_user)

                case "2":
                    while True:
                        print("\n[훈련 기록]")
                        print("1. 훈련 기록 추가")
                        print("2. 훈련 기록 보기")
                        print("3. 뒤로 가기")
                        training_choice = input("선택: ")
                        if training_choice == "3":
                            break
                        execute_training_choice(training_choice, logged_in_user)

                case "3":
                    while True:
                        statistics_menu()
                        stats_choice = input("선택: ")
                        if not execute_statistics_choice(stats_choice):
                            break

                case "4":
                    print("로그아웃 되었습니다.")
                    logged_in_user = None

                case "5":
                    print("WithPaw를 종료합니다. 감사합니다!")
                    break

                case _:
                    print("잘못된 입력입니다. 다시 시도해주세요!")