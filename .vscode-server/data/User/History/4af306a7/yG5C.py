import sqlite3  # SQLite3 데이터베이스 연결
import matplotlib.pyplot as plt  # 데이터 시각화를 위한 라이브러리
from matplotlib import rc
import matplotlib.font_manager as fm

# 한글 폰트 설정
font_path = "/opt/anaconda3/envs/bogdong/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/NanumGothic.otf" # 나눔고딕 폰트 경로 (리눅스 기준)
font = fm.FontProperties(fname=font_path)
rc('font', family=font.get_name())  # matplotlib에 한글 폰트 적용

# 반려동물 통계 시각화 함수
def visualize_pet_statistics():
    """
    반려동물 데이터베이스 정보를 바탕으로 종별 및 나이별 분포를 시각화합니다.
    """
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 반려동물 종별 분포
    cursor.execute("SELECT species, COUNT(*) FROM pets GROUP BY species")  # 종별 개수 가져오기
    species_data = cursor.fetchall()
    species = [row[0] for row in species_data]  # 종 이름 리스트
    species_count = [row[1] for row in species_data]  # 각 종의 개수 리스트

    # 나이별 분포
    cursor.execute("SELECT age, COUNT(*) FROM pets GROUP BY age")  # 나이별 개수 가져오기
    age_data = cursor.fetchall()
    ages = [row[0] for row in age_data]  # 나이 리스트
    age_count = [row[1] for row in age_data]  # 각 나이의 개수 리스트

    conn.close()  # 데이터베이스 연결 종료

    # 반려동물 종별 분포 시각화
    plt.figure(figsize=(10, 5))  # 그래프 크기 설정
    plt.bar(species, species_count, color='skyblue')  # 막대그래프 생성
    plt.title('반려동물 종별 분포', fontproperties=font)  # 제목 설정
    plt.xlabel('종', fontproperties=font)  # X축 라벨
    plt.ylabel('개수', fontproperties=font)  # Y축 라벨
    plt.show()  # 그래프 표시

    # 반려동물 나이별 분포 시각화
    plt.figure(figsize=(10, 5))  # 그래프 크기 설정
    plt.bar(ages, age_count, color='lightgreen')  # 막대그래프 생성
    plt.title('반려동물 나이별 분포', fontproperties=font)  # 제목 설정
    plt.xlabel('나이', fontproperties=font)  # X축 라벨
    plt.ylabel('개수', fontproperties=font)  # Y축 라벨
    plt.show()  # 그래프 표시

# 활동 로그 시각화 *(선택 사항)*: 훈련 기록 시각화
def visualize_training_statistics():
    """
    훈련 기록 데이터를 바탕으로 날짜별 훈련 횟수를 시각화합니다.
    """
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 훈련 날짜별 기록 개수
    cursor.execute("SELECT date, COUNT(*) FROM training_records GROUP BY date")  # 날짜별 훈련 횟수 가져오기
    training_data = cursor.fetchall()
    dates = [row[0] for row in training_data]  # 날짜 리스트
    training_count = [row[1] for row in training_data]  # 각 날짜의 훈련 횟수 리스트

    conn.close()  # 데이터베이스 연결 종료

    # 훈련 기록 시각화
    plt.figure(figsize=(10, 5))  # 그래프 크기 설정
    plt.plot(dates, training_count, marker='o', color='orange')  # 꺾은선 그래프 생성
    plt.title('훈련 기록 통계', fontproperties=font)  # 제목 설정
    plt.xlabel('날짜', fontproperties=font)  # X축 라벨
    plt.ylabel('훈련 횟수', fontproperties=font)  # Y축 라벨
    plt.xticks(rotation=45, fontproperties=font)  # X축 라벨 회전 및 폰트 설정
    plt.tight_layout()  # 그래프 레이아웃 조정
    plt.show()  # 그래프 표시