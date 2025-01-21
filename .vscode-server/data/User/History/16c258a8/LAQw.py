import os

font_path = "/Users/iujeong/Library/Fonts/NanumGothic.otf"
if os.path.exists(font_path):
    print("폰트 경로 확인 완료!")
else:
    print("가상 환경에서 폰트 경로에 접근할 수 없습니다.")


import matplotlib
print(matplotlib.get_data_path())