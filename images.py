# -----------<이미지들>-----------

# 이미지를 load한 변수들을 모아둔 파일

from pico2d import * # pico2d 모듈

# ----- 이미지 변수들 -----

img_beat_small = None
img_beat_big = None

if img_beat_small == None:
    img_beat_small = load_image('img_beat_small.png')

if img_beat_big == None:
    img_beat_big = load_image('img_beat_big.png')