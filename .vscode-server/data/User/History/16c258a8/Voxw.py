import os

font_path = "/Users/iujeong/Library/Fonts/NanumGothic.otf"
if os.path.exists(font_path):
    print("폰트 경로 확인 완료!")
else:
    print("폰트 경로가 잘못되었습니다.")