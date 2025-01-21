from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import initialize_database
from user_management import login, set_user_profile
from pet_management import view_my_pets
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # 세션 암호화 키

# 초기화
initialize_database()

# 홈 페이지
@app.route('/')
def home():
    if 'user_id' in session:  # 로그인 여부 확인
        user_name = session['user_name']
        return render_template('main.html', user_name=user_name)  # 메인 페이지 렌더링
    else:
        return redirect(url_for('login_page'))  # 로그인 페이지로 리디렉션

# 로그인 페이지
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = login(username, password)
        if user:
            session['user_id'] = user[0]  # 세션에 사용자 ID 저장
            session['user_name'] = user[3]  # 세션에 사용자 이름 저장
            flash('로그인 성공!', 'success')
            return redirect(url_for('home'))
        else:
            flash('로그인 실패. 아이디 또는 비밀번호를 확인하세요.', 'danger')
    return render_template('login.html')  # 로그인 HTML 페이지 렌더링

# 반려동물 정보 페이지
@app.route('/pets')
def pets():
    if 'user_id' not in session:
        return redirect(url_for('login_page'))  # 로그인 안 된 경우 리디렉션
    user_id = session['user_id']
    pets = view_my_pets(user_id)  # 사용자 반려동물 정보 가져오기
    return render_template('pet_info.html', pets=pets)  # 반려동물 정보 페이지 렌더링

# 로그아웃
@app.route('/logout')
def logout():
    session.clear()  # 세션 데이터 초기화
    flash('로그아웃되었습니다.', 'info')
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True)