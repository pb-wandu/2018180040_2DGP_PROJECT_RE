# ----------<게임 프레임워크>----------

# 모드 1 - 메인 메뉴

from pico2d import *  # pico2d 모듈 import
import game_framework # 게임 프레임워크

import gamemode_2_0_gamemenu as gamemenu  # 게임 모드 gamemenu 모듈 import
import gamemode_2_1_state    as gamestate # 상태 관련 모듈 import
import gamemode_2_1_gameinfo as gameinfo  # 게임 정보 관련 모듈 import

import game_time # 시간 관련 모듈 import

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

    # 대기중 이미지
    global waitingimage
    waitingimage = load_image('./resource_image/img_gamewaiting.png')

    # 메인메뉴 배경
    global mainmenubg
    mainmenubg = load_image('./resource_image/img_background_mainmenu.png')

    # 게임 타이머에 현재 시간을 시작시간으로 지정
    game_time.gametimer.setStartTime()

    print("### mainmenu 진입")

def finish():
    global waitingimage
    global mainmenubg

    del waitingimage
    del mainmenubg

    # 게임 타이머에 현재 시간을 시작시간으로 지정
    game_time.gametimer.setStartTime()

    # 상태 머신의 현재 상태를 Ready로 지정
    gamestate.state_machine.cur_state = gamestate.Ready

    # 콤보 개수 초기화
    gameinfo.gameinfomation.nowcombo = 0

    print("### mainmenu에서 나가기")

def update():
    ### 임시로 2초 뒤 gamemenu로 넘어가게 함
    if get_time() - game_time.gametimer.start_time >= 2.0:
        # 게임 타이머에 현재 시간을 시작시간으로 지정
        game_time.gametimer.setStartTime()
        # gamemenu로 현재 모드 변경
        game_framework.change_mode(gamemenu)

def draw():
    global waitingimage
    global mainmenubg

    clear_canvas()
    mainmenubg.draw(400, 300, 800, 600)  # 배경 그리기
    waitingimage.draw(800 // 2, 600 // 2)
    update_canvas()
    pass

def pause():
    pass

def resume():
    pass