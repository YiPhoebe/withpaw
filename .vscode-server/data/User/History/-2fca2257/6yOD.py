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

if __name__ == "__main__":  # 프로그램의 진입점, main 루프를 실행
    initialize_database()   # 데이터 베이스 초기화

    logged_in_user = None   # 로그인 상태를 저장하는 변수

    while True:     # 메인 루프 시작
        if not logged_in_user:  # 로그인 상태가 아닌 경우 메인 메뉴 표시
            main_menu()     # 메인 메뉴 출력
            choice = input("선택: ")    # 사용자 입력 받기

            if choice == "1":   