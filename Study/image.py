import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.font_manager as fm

# 한글 폰트 경로 설정
font_path = "/opt/anaconda3/envs/bogdong/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/NanumGothic.otf"  # 실제 폰트 경로 입력
font_prop = fm.FontProperties(fname=font_path)
rc('font', family=font_prop.get_name())  # 폰트 적용

# 그래프 생성
def test_plot():
    labels = ['A', 'B', 'C', 'D']  # X축 레이블
    values = [10, 20, 15, 25]  # Y축 값

    plt.figure(figsize=(8, 6))  # 그래프 크기 설정
    plt.bar(labels, values, color='skyblue')  # 막대 그래프 생성
    plt.title('테스트 그래프', fontproperties=font_prop)  # 제목 설정
    plt.xlabel('카테고리', fontproperties=font_prop)  # X축 라벨
    plt.ylabel('값', fontproperties=font_prop)  # Y축 라벨
    plt.tight_layout()  # 레이아웃 정리
    plt.show()  # 그래프 표시

# 테스트 실행
if __name__ == "__main__":
    test_plot()