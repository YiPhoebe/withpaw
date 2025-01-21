import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.font_manager as fm

# 폰트 경로 설정
font_path = "/opt/anaconda3/envs/bogdong/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/NanumGothic.otf"
font = fm.FontProperties(fname=font_path)

# matplotlib에 폰트 적용
rc('font', family=font.get_name())

# 그래프 테스트
plt.figure()
plt.title('테스트 그래프', fontproperties=font)
plt.plot([1, 2, 3], [4, 5, 6], label='테스트 라인')
plt.legend()
plt.show()