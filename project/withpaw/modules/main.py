from database import initialize_database    # 데이터베이스 초기화 관련 함수를 가져옴
from user_management import set_user_profile, login, find_username, find_password   # 사용자 관리 관련 함수 (프로필 생성, 로그인, 아이디/비밀번호 찾기)
from pet_management import add_pet, update_pet, delete_pet, update_pet_notes, view_my_pets  #  반려동물 관리 관련 함수 (등록, 수정, 삭제, 조회)
from training_management import add_training_record, view_training_records    # 훈련 기록 관리 함수 (추가 및 조회)

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

def main_meun():    # 메인 메뉴를 출력하는 함수
    print("\n1. 사용자 프로필 생성")
    print("2. 로그인")
    print("3. 종료")

def family_menu(logged_in_user):  # 나의 가족 보기 메뉴를 출력하는 함수
    """
    나의 가족 보기 메뉴: 반려동물 정보를 바로 보여주고, 추가 작업을 선택하도록 구성
    """
    print("\n[나의 가족 보기]")
    pets = view_my_pets(logged_in_user[0])  # 반려동물 정보를 가져옵니다.
    
    if pets:
        print("\n나의 반려동물 목록:")
        for pet in pets:
            print(f"이름: {pet[0]}, 나이: {pet[1]}, 종: {pet[2]}, 품종: {pet[3]}")
    else:
        print("\n등록된 반려동물이 없습니다.")  # 반려동물이 없을 경우에만 출력됩니다.

    print("\n1. 반려동물 정보 등록 및 추가")
    print("2. 반려동물 정보 수정")
    print("3. 뒤로 가기")

def execute_family_choice(choice, logged_in_user):
    """
    나의 가족 보기 메뉴에서 선택된 작업을 실행
    """
    match choice:
        case "1":
            add_pet
        case "2":
            pets = view_my_pets(logged_in_user[0])
            if not pets:
                print("수정할 반려동물이 없습니다. 먼저 반려동물을 등록해주세요.")
                return True
            
            print("수정할 반려동물을 선택하세요 : ")
            for idx,  pet in enumerate(pets, start=1):
                print(f"{idx}. {pet[0]} (나이 : {pet[1]}), 종 : {pet[2]}, 품종 : {pet[3]}")

            try:
                selected = int(input("선택 (번호입력) : )"))
                if 1 <= selected <= len(pets):
                    update_pet(pets[selected - 1])
                else:
                    print("잘못된 선택입니다.")
            except ValueError:
                print("숫자를 입력하세요.")
        case "3":
            return False
        case _:
            print("잘못된 입력입니다. 다시 시도해주세요.")
    return True

def training_menu(logged_in_user):  # 훈련 기록 메뉴를 출력하는 함수
    """
    훈련 기록 메뉴 : 훈련 시작과 기존 기록 조회 옵션 제공
    """
    while True:
        print("\n[훈련 기록]")
        print("1. 훈련 시작!")
        print("2. 훈련 기록 보기")
        print("3. 뒤로 가기")

        choice = input("선택: ")
        match choice:
            case "1":
                print("훈련을 시작합니다!")
                add_training_record(logged_in_user[0])
            case "2":
                print("훈련 기록을 불러옵니다.")
                view_training_records(logged_in_user[0])
            case "3":
                print("이전 메뉴로 돌아갑니다.")
                break
            case _:
                print("잘못된 입력입니다. 다시 시도해주세요.")

def main():
    initialize_database()

    logged_in_user = None

    while True:
        if not logged_in_user:
            main_meun()
            choice = input("선택 : ")

            match choice:
                case "1":
                    set_user_profile()
                case "2":
                    logged_in_user = login()
                    if not logged_in_user:
                        print("로그인에 실패했습니다. 아이디나 비밀번호를 확인해주세요.")
                        print("1. 아이디 찾기")
                        print("2. 비밀번호 찾기")
                        recovery_choice = input("선택 : ")
                        match recovery_choice:
                            case "1":
                                find_username()
                            case "2":
                                find_password()
                            case _:
                                print("잘못된 입력입니다. 메인 메뉴로 돌아갑니다.")

                case "3":
                    print("WithPaw를 종료합니다. 감사합니다!")
                    break
                case _:
                    print("잘못된 입력입니다. 다시 시도해주세요.")

        else:
            print(f"\n안녕하세요, {logged_in_user[3]}님!")
            print("1. 나의가족 보기")
            print("2. 로그아웃")
            print("3. 종료")

            choice = input("선택 : ")

            match choice:
                case "1":
                    while True:
                        family_menu(logged_in_user)
                        family_choice = input("선택 : ")
                        if not execute_family_choice(family_choice, logged_in_user):
                            break
                case "2":
                    print("로그아웃 되었습니다.")
                    logged_in_user = None
                case "3":
                    print("WithPaw를 종료합니다. 감사합니다!")
                    break
                case _:
                    print("잘못된 입력입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()