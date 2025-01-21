import matplotlib
from matplotlib import font_manager as fm

# 캐시를 강제 초기화
matplotlib.get_cachedir()  # 캐시 경로 확인
fm._rebuild()  # 폰트 캐시 강제 재생성

print("폰트 캐시를 재생성했습니다.")