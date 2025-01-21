import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager as fm

# 폰트 경로
font_path = "/opt/anaconda3/envs/bogdong/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/NanumGothic.otf"
font = fm.FontProperties(fname=font_path)

# matplotlib에 폰트 설정
rc('font', family=font.get_name())

# 테스트 그래프
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("테스트 그래프", fontproperties=font)
plt.show()