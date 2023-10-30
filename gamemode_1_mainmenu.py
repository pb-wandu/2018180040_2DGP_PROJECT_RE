# ----------<게임 프레임워크>----------

# 모드 1 - 메인 메뉴

from pico2d import *  # pico2d 모듈 import
import game_framework # 게임 프레임워크

import gamemode_2_gamemenu # 게임 모드 gamemenu 모듈 import

# ----- 게임 프레임워크 동작 함수들 -----

def init():
    global tempimage
    global start_time
    tempimage = load_image('img_gamewaiting.png')
    start_time = get_time()

    print("### mainmenu 진입")

def finish():
    global tempimage
    del tempimage

    print("### mainmenu에서 나가기")

def update():
    global start_time
    ### 임시로 2초 뒤 gamemenu로 넘어가게 함
    if get_time() - start_time >= 2.0:
        start_time = get_time()
        game_framework.change_mode(gamemode_2_gamemenu)

def draw():
    global tempimage
    clear_canvas()
    tempimage.draw(800//2, 600//2)
    update_canvas()
    pass

def handle_events():
    pass

def pause():
    pass

def resume():
    pass