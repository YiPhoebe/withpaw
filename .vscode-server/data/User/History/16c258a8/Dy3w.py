import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.font_manager as fm

# 폰트 경로 설정
font_path = "/opt/anaconda3/envs/bogdong/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/NanumGothic.otf"
font = fm.FontProperties(fname=font_path)  # FontProperties 객체 생성
rc('font', family=font.get_name())  # Matplotlib에 폰트 적용

# 테스트 그래프
plt.title("한글 폰트 테스트", fontproperties=font)  # 제목에 폰트 적용
plt.plot([1, 2, 3], [4, 5, 6])  # 간단한 플롯
plt.show()