import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.font_manager as fm

# 한글 폰트 경로 설정 (NanumGothic 예시)
font_path = "/opt/anaconda3/envs/bogdong/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/NanumGothic.otf"
font = fm.FontProperties(fname=font_path)  # 폰트 속성 생성
rc('font', family=font.get_name())  # matplotlib에 폰트 적용

# 테스트 그래프
plt.figure()
plt.title("한글 테스트", fontproperties=font)  # 제목에 한글 사용
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()