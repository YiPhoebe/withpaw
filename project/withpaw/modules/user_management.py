import sqlite3

def set_user_profile():  # 사용자 프로필 생성 함수
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    username = input("사용할 아이디를 입력하세요: ")
    cursor.execute("SELECT * FROM user_profile WHERE username = ?", (username,))
    if cursor.fetchone():
        print("이미 존재하는 아이디입니다!")
        conn.close()
        return

    password = input("비밀번호를 입력하세요: ")
    name = input("이름을 입력하세요: ")
    email = input("이메일을 입력하세요 (선택 사항): ")

    cursor.execute("""
    INSERT INTO user_profile (username, password, name, email)
    VALUES (?, ?, ?, ?)
    """, (username, password, name, email))

    conn.commit()  # 변경 사항 저장
    conn.close()   # 데이터베이스 연결 종료
    print(f"사용자 프로필이 생성되었습니다! 아이디: {username}")

def login():  # 사용자 로그인 함수
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")

    cursor.execute("SELECT * FROM user_profile WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()  # 일치하는 사용자 정보 가져오기
    conn.close()  # 데이터베이스 연결 종료

    if user:
        return user
    else:
        return None

def find_username():  # 아이디 찾기 함수
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    email = input("등록된 이메일을 입력하세요: ")

    cursor.execute("SELECT username FROM user_profile WHERE email = ?", (email,))
    user = cursor.fetchone()  # 이메일에 해당하는 아이디 검색
    conn.close()  # 데이터베이스 연결 종료

    if user:
        print(f"등록된 아이디는: {user[0]}입니다.")  # 아이디 출력
    else:
        print("등록된 이메일이 없습니다.")  # 이메일 미등록 알림

def find_password():  # 비밀번호 찾기 함수
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    username = input("아이디를 입력하세요: ")
    email = input("등록된 이메일을 입력하세요: ")

    cursor.execute("SELECT password FROM user_profile WHERE username = ? AND email = ?", (username, email))
    user = cursor.fetchone()  # 아이디와 이메일에 해당하는 비밀번호 검색
    conn.close()  # 데이터베이스 연결 종료

    if user:
        print(f"비밀번호는: {user[0]}입니다.")  # 비밀번호 출력
    else:
        print("아이디 또는 이메일이 잘못되었습니다.")  # 오류 메시지 출력