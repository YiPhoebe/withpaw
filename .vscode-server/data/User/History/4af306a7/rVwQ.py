import sqlite3  # SQLite3 데이터베이스 연결
import matplotlib.pyplot as plt  # 데이터 시각화를 위한 라이브러리

# 반려동물 통계 시각화 함수
def visualize_pet_statistics():
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 반려동물 종별 분포
    cursor.execute("SELECT species, COUNT(*) FROM pets GROUP BY species")
    species_data = cursor.fetchall()
    species = [row[0] for row in species_data]
    species_count = [row[1] for row in species_data]

    # 나이별 분포
    cursor.execute("SELECT age, COUNT(*) FROM pets GROUP BY age")
    age_data = cursor.fetchall()
    ages = [row[0] for row in age_data]
    age_count = [row[1] for row in age_data]

    conn.close()  # 데이터베이스 연결 종료

    # 반려동물 종별 분포 시각화
    plt.figure(figsize=(10, 5))
    plt.bar(species, species_count, color='skyblue')
    plt.title('반려동물 종별 분포')
    plt.xlabel('종')
    plt.ylabel('개수')
    plt.show()

    # 반려동물 나이별 분포 시각화
    plt.figure(figsize=(10, 5))
    plt.bar(ages, age_count, color='lightgreen')
    plt.title('반려동물 나이별 분포')
    plt.xlabel('나이')
    plt.ylabel('개수')
    plt.show()

# 활동 로그 시각화 *(선택 사항)*: 훈련 기록 시각화
def visualize_training_statistics():
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 훈련 날짜별 기록 개수
    cursor.execute("SELECT date, COUNT(*) FROM training_records GROUP BY date")
    training_data = cursor.fetchall()
    dates = [row[0] for row in training_data]
    training_count = [row[1] for row in training_data]

    conn.close()  # 데이터베이스 연결 종료

    # 훈련 기록 시각화
    plt.figure(figsize=(10, 5))
    plt.plot(dates, training_count, marker='o', color='orange')
    plt.title('훈련 기록 통계')
    plt.xlabel('날짜')
    plt.ylabel('훈련 횟수')
    plt.xticks(rotation=45)  # 날짜 라벨 회전
    plt.tight_layout()
    plt.plot([1,2,3],[4,5,6])
    plt.show()