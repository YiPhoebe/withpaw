import sqlite3

# 사용자 프로필 생성 함수
def set_user_profile():
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 사용자 아이디 입력 받기
    username = input("사용할 아이디를 입력하세요: ")
    cursor.execute("SELECT * FROM user_profile WHERE username = ?", (username,))
    if cursor.fetchone():
        print("이미 존재하는 아이디입니다!")  # 중복 아이디 처리
        conn.close()
        return

    # 사용자 비밀번호, 이름, 이메일 입력 받기
    password = input("비밀번호를 입력하세요: ")
    name = input("이름을 입력하세요: ")
    email = input("이메일을 입력하세요 (선택 사항): ")

    # 사용자 정보를 데이터베이스에 삽입
    cursor.execute("""
    INSERT INTO user_profile (username, password, name, email)
    VALUES (?, ?, ?, ?)
    """, (username, password, name, email))

    conn.commit()  # 변경 사항 저장
    conn.close()   # 데이터베이스 연결 종료
    print(f"사용자 프로필이 생성되었습니다! 아이디: {username}")

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