import sqlite3  # SQLite3 모듈 가져오기
from datetime import datetime  # 날짜 유효성 검사를 위한 datetime 모듈 가져오기

# 훈련 기록 테이블 초기화 함수
def initialize_training_table():
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 훈련 기록 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS training_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pet_id INTEGER NOT NULL,
        description TEXT,
        date TEXT,
        success INTEGER,
        FOREIGN KEY(pet_id) REFERENCES pets(id)
    )
    """)

    conn.commit()
    conn.close()
    print("훈련 기록 테이블이 성공적으로 생성되었습니다!")

# 날짜 유효성 검사 함수
def get_valid_date():
    while True:
        date_input = input("훈련 날짜를 입력하세요 (예: YYYY-MM-DD): ")
        try:
            datetime.strptime(date_input, "%Y-%m-%d")  # 날짜 형식 검사
            return date_input  # 유효한 날짜 반환
        except ValueError:
            print("유효하지 않은 날짜 형식입니다. 다시 입력해주세요.")  # 오류 메시지 출력

# 훈련 기록 추가 함수
def add_training_record(user_id):  # 로그인한 사용자 ID를 매개변수로 받음
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 사용자별 반려동물 목록 가져오기
    cursor.execute("SELECT id, name FROM pets WHERE family_id = ?", (user_id,))
    pets = cursor.fetchall()

    if not pets:  # 반려동물이 없는 경우 처리
        print("등록된 반려동물이 없습니다. 먼저 반려동물을 등록해주세요.")
        conn.close()
        return

    print("\n훈련 기록을 추가할 반려동물을 선택하세요:")
    for pet in pets:
        print(f"ID: {pet[0]}, 이름: {pet[1]}")

    # 반려동물 ID 입력 받기
    try:
        pet_id = int(input("반려동물 ID를 입력하세요: "))
        if not any(pet[0] == pet_id for pet in pets):  # 유효한 ID인지 확인
            print("유효하지 않은 반려동물 ID입니다.")
            conn.close()
            return
    except ValueError:
        print("숫자를 입력해주세요.")
        conn.close()
        return

    # 훈련 기록 입력
    description = input("훈련 내용을 입력하세요: ")  # 훈련 기록 설명 입력
    date = get_valid_date()  # 날짜 유효성 검사 및 입력
    success = get_training_success()  # 훈련 성공 여부 입력

    # 훈련 기록 삽입
    cursor.execute("""
    INSERT INTO training_records (pet_id, date, description, success)
    VALUES (?, ?, ?, ?)
    """, (pet_id, date, description, int(success)))
    conn.commit()  # 변경 사항 저장
    conn.close()
    print("훈련 기록이 성공적으로 추가되었습니다!")

# 훈련 성공 여부 입력 함수
def get_training_success():
    while True:
        success = input("훈련 성공 여부를 입력하세요 (y/n): ").lower()
        if success in ('y', 'n'):  # y/n 유효성 검사
            return success == 'y'  # 성공이면 True, 실패면 False 반환
        else:
            print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")

# 훈련 기록 보기 함수
def view_training_records(user_id):
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 사용자 ID에 해당하는 훈련 기록 조회
    cursor.execute("""
    SELECT pets.name, training_records.description, training_records.date, training_records.success
    FROM training_records
    JOIN pets ON training_records.pet_id = pets.id
    WHERE pets.family_id = ?
    """, (user_id,))
    records = cursor.fetchall()

    if records:  # 기록이 있는 경우 출력
        print("\n훈련 기록 목록:")
        for record in records:
            status = "성공" if record[3] == 1 else "실패"  # 성공 여부 표시
            print(f"반려동물 이름: {record[0]}, 훈련 내용: {record[1]}, 날짜: {record[2]}, 결과: {status}")
    else:
        print("\n훈련 기록이 없습니다.")  # 기록이 없는 경우 메시지 출력

    conn.close()  # 데이터베이스 연결 종료