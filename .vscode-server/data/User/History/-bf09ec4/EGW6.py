import sqlite3  # SQLite3 데이터베이스 연결
import matplotlib.pyplot as plt  # 데이터 시각화를 위한 라이브러리
import os  # 운영체제 명령어를 실행하기 위한 라이브러리

# 반려동물 통계 시각화 및 저장 함수
def visualize_pet_statistics(output_path="pet_statistics.png"):
    """
    반려동물 통계를 시각화하고 이미지로 저장합니다.
    """
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 반려동물 종별 분포
    cursor.execute("SELECT species, COUNT(*) FROM pets GROUP BY species")
    species_data = cursor.fetchall()
    species = [row[0] for row in species_data]
    species_count = [row[1] for row in species_data]

    conn.close()  # 데이터베이스 연결 종료

    # 반려동물 종별 분포 시각화 및 저장
    plt.figure(figsize=(10, 5))
    plt.bar(species, species_count, color='skyblue')
    plt.title('반려동물 종별 분포')
    plt.xlabel('종')
    plt.ylabel('개수')
    plt.tight_layout()
    plt.savefig(output_path)  # 그래프 저장
    plt.close()

    print(f"반려동물 통계 그래프가 '{output_path}'에 저장되었습니다.")

    # 저장된 그래프 파일 열기
    try:
        if os.name == 'posix':  # macOS, Linux
            os.system(f"open {output_path}")
        elif os.name == 'nt':  # Windows
            os.startfile(output_path)
        else:
            print("현재 OS에서 자동 열기를 지원하지 않습니다. 파일을 수동으로 열어주세요.")
    except Exception as e:
        print(f"그래프를 여는 중 오류가 발생했습니다: {e}")

# 훈련 기록 시각화 및 저장 함수
def visualize_training_statistics(output_path="training_statistics.png"):
    """
    훈련 기록 통계를 시각화하고 이미지로 저장한 후, 저장된 이미지를 엽니다.
    """
    conn = sqlite3.connect("withpaw.db")  # 데이터베이스 연결
    cursor = conn.cursor()

    # 훈련 날짜별 기록 개수
    cursor.execute("SELECT date, COUNT(*) FROM training_records GROUP BY date")
    training_data = cursor.fetchall()
    dates = [row[0] for row in training_data]
    training_count = [row[1] for row in training_data]

    conn.close()  # 데이터베이스 연결 종료

    # 훈련 기록 시각화 및 저장
    plt.figure(figsize=(10, 5))
    plt.plot(dates, training_count, marker='o', color='orange')
    plt.title('훈련 기록 통계')
    plt.xlabel('날짜')
    plt.ylabel('훈련 횟수')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)  # 그래프 저장
    plt.close()

    print(f"훈련 기록 통계 그래프가 '{output_path}'에 저장되었습니다.")

    # 저장된 그래프 파일 열기
    try:
        if os.name == 'posix':  # macOS, Linux
            os.system(f"open {output_path}")
        elif os.name == 'nt':  # Windows
            os.startfile(output_path)
        else:
            print("현재 OS에서 자동 열기를 지원하지 않습니다. 파일을 수동으로 열어주세요.")
    except Exception as e:
        print(f"그래프를 여는 중 오류가 발생했습니다: {e}")
