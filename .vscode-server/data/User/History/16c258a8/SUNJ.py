from matplotlib import font_manager as fm

font_path = "/opt/anaconda3/envs/bogdong/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/NanumGothic.otf"
font = fm.FontProperties(fname=font_path)

print("Font Name:", font.get_name())  # 폰트 이름 출력