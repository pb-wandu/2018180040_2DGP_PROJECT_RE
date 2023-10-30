# ----------<main 파일>----------

# 실제 실행(main) 부분 코드를 기록한 파일

from pico2d import *  # pico2d 모듈 import
# import game_world   # world 전체 관련 내용 모듈 import
import game_framework # 게임 프레임워크

# 게임 모드
import gamemode_1_mainmenu as startmode # 메인메뉴 모드
import gamemode_2_gamemenu              # 게임메뉴 모드

# ----- 실제 게임 실행 부분 -----

open_canvas(800, 600)

# game_framework.run(startmode) # <- 실제로는 여기부터 실행함
game_framework.run(gamemode_2_gamemenu)

close_canvas()