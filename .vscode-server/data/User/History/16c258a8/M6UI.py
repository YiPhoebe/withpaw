import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.font_manager as fm

# 폰트 경로 설정 (확실히 존재하는 경로 사용)
font_path = "/home/iujeong/.cache/matplotlib/mpl-data/fonts/ttf/NanumGothic.otf"
font = fm.FontProperties(fname=font_path)  # FontProperties 객체 생성
rc('font', family=font.get_name())  # Matplotlib에 폰트 적용

# 테스트 그래프
plt.title("한글 폰트 테스트", fontproperties=font)  # 제목에 폰트 적용
plt.plot([1, 2, 3], [4, 5, 6])  # 간단한 플롯
plt.show()