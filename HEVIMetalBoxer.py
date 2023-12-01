# ----------<main 파일>----------

# 실제 실행(main) 부분 코드를 기록한 파일

import pico2d # pico2d 모듈 import
import os

import game_world   # world 전체 관련 내용 모듈 import
import game_framework # 게임 프레임워크

# pico2d가 활용하는 SDL 라이브러리 DLL
# print("SDL 라이브러리 DLL 받아오기 (경로) : " + str(os.getenv('PYSDL2_DLL_PATH')))
# <수정사항> os.getenv로 했을 때 작동이 안 되어 해당 경로의 파일을 전부 pico2d 안에 넣었습니다

# 게임 모드
import gamemode_1_0_mainmenu as startmode # 메인메뉴 모드
import gamemode_2_0_gamemenu              # 게임메뉴 모드

# >> 설치시 터미널에서 pyinstaller -F HEVIMetalBoxer.py 실행하기

# ----- 실제 게임 실행 부분 -----

pico2d.open_canvas(800, 600)

# game_framework.run(startmode) # <- 실제로는 여기부터 실행함
game_framework.run(gamemode_2_0_gamemenu)

pico2d.close_canvas()