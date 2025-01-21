import sqlite3

# 사용자 프로필 생성 함수
def set_user_profile():
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 사용자 ID 입력 (중복 방지 및 유효성 검사)
    while True:
        try:
            user_id = int(input("사용할 ID를 입력하세요 (숫자): "))
            if user_id <= 0:
                print("ID는 0보다 큰 숫자여야 합니다. 다시 입력하세요.")
                continue

            cursor.execute("SELECT * FROM user_profile WHERE id = ?", (user_id,))
            if cursor.fetchone():
                print("이미 사용 중인 ID입니다. 다른 ID를 입력하세요.")
            else:
                break
        except ValueError:
            print("유효한 숫자를 입력하세요.")

    # 사용자 아이디, 비밀번호, 이름, 이메일 입력 받기
    username = input("사용할 아이디를 입력하세요: ")
    cursor.execute("SELECT * FROM user_profile WHERE username = ?", (username,))
    if cursor.fetchone():
        print("이미 존재하는 아이디입니다!")
        conn.close()
        return

    password = input("비밀번호를 입력하세요: ")
    name = input("이름을 입력하세요: ")
    email = input("이메일을 입력하세요 (선택 사항): ")

    # 사용자 정보를 데이터베이스에 삽입
    cursor.execute("""
    INSERT INTO user_profile (id, username, password, name, email)
    VALUES (?, ?, ?, ?, ?)
    """, (user_id, username, password, name, email))

    conn.commit()  # 변경 사항 저장
    conn.close()   # 데이터베이스 연결 종료
    print(f"사용자 프로필이 생성되었습니다! ID: {user_id}, 아이디: {username}")

# 사용자 로그인 함수
def login():
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 사용자 아이디와 비밀번호 입력 받기
    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")

    # 사용자 정보 확인
    cursor.execute("SELECT * FROM user_profile WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()  # 일치하는 사용자 정보 가져오기
    conn.close()  # 데이터베이스 연결 종료

    if user:
        print(f"로그인 성공! 환영합니다, {user[3]}님!")  # 성공 메시지
        return user
    else:
        print("로그인 실패! 아이디와 비밀번호를 확인해주세요.")  # 실패 메시지
        return None

# 사용자 프로필 보기 함수
def view_user_profile(user_id):
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 사용자 프로필 조회
    cursor.execute("SELECT id, username, name, email FROM user_profile WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    conn.close()  # 데이터베이스 연결 종료

    if user:
        print("\n사용자 프로필 정보:")
        print(f"ID: {user[0]}")
        print(f"아이디: {user[1]}")
        print(f"이름: {user[2]}")
        print(f"이메일: {user[3] if user[3] else '없음'}")
    else:
        print("사용자 프로필을 찾을 수 없습니다.")
