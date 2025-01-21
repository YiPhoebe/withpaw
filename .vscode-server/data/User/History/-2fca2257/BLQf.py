from database import initialize_database
from user_management import set_user_profile, login
from pet_management import add_pet, update_pet, delete_pet, view_my_pets
from training_management import add_training_record, view_training_records

def main_menu():
    print("\n1. 사용자 프로필 생성")
    print("2, 로그인")
    print("3. 종료")

def family_menu():
    print("\n[나의 가족 보기]]")
    print("1. 반려동물 등록")
    print("2. 반려동물 정보 수정")
    print("3. 반려동물 정보 삭제")
    print("4. 나의 반려동물 보기")
    print("5. 뒤로 가기")

def training_menu():
    print("\n[훈련 기록]")
    print("1. 훈련 기록 추가")
    print("2. 훈련 기록 보기")