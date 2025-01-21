from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 홈 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 훈련 기록 보기
@app.route('/view_training')
def view_training():
    # 데이터베이스에서 훈련 기록을 가져오는 로직 추가
    training_records = [
        {"name": "강아지1", "description": "앉아 훈련", "date": "2025-01-21"},
        {"name": "강아지2", "description": "손 훈련", "date": "2025-01-22"},
    ]
    return render_template('view_training.html', records=training_records)

if __name__ == "__main__":
    app.run(debug=True)