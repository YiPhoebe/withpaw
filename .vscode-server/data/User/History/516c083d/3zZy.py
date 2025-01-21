import sqlite3  # 데이터베이스 연결
import matplotlib.pyplot as plt  # 데이터 시각화를 위한 라이브러리
from matplotlib import rc
import matplotlib.font_manager as fm
import os  # 파일 열기를 위한 OS 모듈
import sys
sys.path.append('/path/to/your/project')

from database import initialize_database  # 데이터베이스 초기화 관련 함수
from project.web.static.user_management import set_user_profile, login, find_username, find_password  # 사용자 관리 함수 (프로필 생성, 로그인, 아이디/비밀번호 찾기)
from project.web.static.pet_management import add_pet, update_pet, delete_pet, update_pet_notes, view_my_pets  # 반려동물 관리 함수 (등록, 수정, 삭제, 조회)
from project.web.static.training_management import add_training_record, view_training_records  # 훈련 기록 관리 함수 (추가 및 조회)
from PIL import Image

# 이미지 열기
img = Image.open("training_statistics.png")

# 이미지 표시
img.show()

# 반려동물 통계 시각화 및 저장 함수
def visualize_pet_statistics(output_path="pet_statistics.png"):
    """
    반려동물 통계를 시각화하고 이미지로 저장합니다.
    저장된 이미지를 자동으로 엽니다.
    """
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 반려동물 종별 분포
    cursor.execute("SELECT species, COUNT(*) FROM pets GROUP BY species")
    species_data = cursor.fetchall()
    species = [row[0] for row in species_data]
    species_count = [row[1] for row in species_data]

    conn.close()  # 데이터베이스 연결 종료

    # 반려동물 종별 분포 시각화 및 저장
    plt.figure(figsize=(10, 5))
    plt.bar(species, species_count, color='skyblue')
    plt.title('반려동물 종별 분포')
    plt.xlabel('종')
    plt.ylabel('개수')
    plt.tight_layout()
    plt.savefig(output_path)  # 그래프 저장
    plt.close()

    print(f"반려동물 통계 그래프가 '{output_path}'에 저장되었습니다.")

    # 저장된 그래프 파일 열기
    try:
        if os.name == 'posix':  # macOS, Linux
            os.system(f"open {output_path}")
        elif os.name == 'nt':  # Windows
            os.startfile(output_path)
        else:
            print("현재 OS에서 자동 열기를 지원하지 않습니다. 파일을 수동으로 열어주세요.")
    except Exception as e:
        print(f"그래프를 여는 중 오류가 발생했습니다: {e}")

# 훈련 기록 시각화 및 저장 함수
def visualize_training_statistics(output_path="training_statistics.png"):
    """
    훈련 기록 통계를 시각화하고 이미지로 저장한 후, 저장된 이미지를 엽니다.
    """
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 훈련 날짜별 기록 개수
    cursor.execute("SELECT date, COUNT(*) FROM training_records GROUP BY date")
    training_data = cursor.fetchall()
    dates = [row[0] for row in training_data]
    training_count = [row[1] for row in training_data]

    conn.close()  # 데이터베이스 연결 종료

    # 훈련 기록 시각화 및 저장
    plt.figure(figsize=(10, 5))
    plt.plot(dates, training_count, marker='o', color='orange')
    plt.title('훈련 기록 통계')
    plt.xlabel('날짜')
    plt.ylabel('훈련 횟수')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)  # 그래프 저장
    plt.close()

    print(f"훈련 기록 통계 그래프가 '{output_path}'에 저장되었습니다.")

    # 저장된 그래프 파일 열기
    try:
        if os.name == 'posix':  # macOS, Linux
            os.system(f"open {output_path}")
        elif os.name == 'nt':  # Windows
            os.startfile(output_path)
        else:
            print("현재 OS에서 자동 열기를 지원하지 않습니다. 파일을 수동으로 열어주세요.")
    except Exception as e:
        print(f"그래프를 여는 중 오류가 발생했습니다: {e}")

def main_menu():  # 메인 메뉴 출력
    print("\n1. 사용자 프로필 생성")
    print("2. 로그인")
    print("3. 아이디 찾기")
    print("4. 비밀번호 찾기")
    print("5. 종료")

def family_menu():  # 나의 가족 보기 메뉴 출력
    print("\n[나의 가족 보기]")
    print("1. 반려동물 정보 등록")
    print("2. 반려동물 정보 수정")
    print("3. 반려동물 정보 삭제")
    print("4. 나의 반려동물 보기")
    print("5. 반려동물 특성 추가")
    print("6. 뒤로 가기")

def training_menu():  # 훈련 기록 메뉴 출력
    print("\n[훈련 기록]")
    print("1. 훈련 기록 추가")
    print("2. 훈련 기록 보기")
    print("3. 뒤로 가기")

def execute_family_choice(choice, logged_in_user):  # 나의 가족 보기 메뉴 선택 실행
    match choice:
        case "1":
            add_pet()
        case "2":
            update_pet()
        case "3":
            delete_pet()
        case "4":
            view_my_pets(logged_in_user[0])
        case "5":
            update_pet_notes()
        case "6":
            return False
        case _:
            print("잘못된 입력입니다. 다시 시도해주세요!")
    return True

def execute_training_choice(choice, logged_in_user):  # 훈련 기록 메뉴 선택 실행
    match choice:
        case "1":
            add_training_record(logged_in_user[0])
        case "2":
            view_training_records(logged_in_user[0])
        case "3":
            return False
        case _:
            print("잘못된 입력입니다. 다시 시도해주세요!")
    return True

def main():  # 프로그램 메인 루프
    initialize_database()

    logged_in_user = None

    while True:
        if not logged_in_user:
            main_menu()
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
                        family_menu()
                        family_choice = input("선택: ")
                        if not execute_family_choice(family_choice, logged_in_user):
                            break
                case "2":
                    while True:
                        training_menu()
                        training_choice = input("선택: ")
                        if not execute_training_choice(training_choice, logged_in_user):
                            break
                case "3":
                    print("1. 반려동물 통계 시각화")
                    print("2. 훈련 기록 통계 시각화")
                    visualization_choice = input("선택: ")
                    if visualization_choice == "1":
                        visualize_pet_statistics()
                    elif visualization_choice == "2":
                        visualize_training_statistics()
                    else:
                        print("잘못된 입력입니다. 다시 시도해주세요!")
                case "4":
                    print("로그아웃 되었습니다.")
                    logged_in_user = None
                case "5":
                    print("WithPaw를 종료합니다. 감사합니다!")
                    break
                case _:
                    print("잘못된 입력입니다. 다시 시도해주세요!")

if __name__ == "__main__":
    main()