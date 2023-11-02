# ----------<게임 프레임워크>----------

# 모드 1 - 메인 메뉴

from pico2d import *  # pico2d 모듈 import
import game_framework # 게임 프레임워크

import gamemode_2_0_gamemenu # 게임 모드 gamemenu 모듈 import
import gamemode_2_1_state as gamestate

# ----- 게임 프레임워크 동작 함수들 -----

# 이벤트에 따른 동작 수행
def handle_events():

    events = get_events()

    for event in events:
        # SDL_QUIT일 경우 게임 종료
        if event.type == SDL_QUIT:
            game_framework.quit()

        # esc키 누를 경우 게임 종료
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

        # 그 외
        else:
            pass

def init():
    global tempimage ### 나중에 수정할 것
    tempimage = load_image('img_gamewaiting.png')
    gamestate.start_time = get_time()

    print("### mainmenu 진입")

def finish():
    global tempimage

    del tempimage
    gamestate.start_time = get_time() # 게임 시작 시간 지정

    print("### mainmenu에서 나가기")

def update():
    ### 임시로 2초 뒤 gamemenu로 넘어가게 함
    if get_time() - gamestate.start_time >= 2.0:
        gamestate.start_time = get_time()
        game_framework.change_mode(gamemode_2_0_gamemenu)

def draw():
    global tempimage
    clear_canvas()
    tempimage.draw(800//2, 600//2)
    update_canvas()
    pass

def pause():
    pass

def resume():
    pass