import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager as fm

# 폰트 경로와 설정
font_path = "/opt/anaconda3/envs/bogdong/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/NanumGothic.otf"
font = fm.FontProperties(fname=font_path)

# Matplotlib 기본 폰트 설정
rc('font', family=font.get_name())

# 확인
print("적용된 폰트 이름:", font.get_name())

# 테스트 그래프
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("테스트: 한글 폰트")
plt.xlabel("X축")
plt.ylabel("Y축")
plt.show()