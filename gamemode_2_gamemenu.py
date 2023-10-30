# ----------<게임 프레임워크>----------

# 모드 2 - 게임 메뉴

# ----- 모듈 import -----

from pico2d import *    # pico2d 모듈 import
import objects          # 상태 머신 및 오브젝트 모듈 import

import game_world
import game_framework

import gamemode_1_mainmenu # 게임 모드 mainmenu 모듈 import

# '모드 2 - 게임 메뉴'용 상태 머신 import
# gamemenu 내에서의 세부 상태 (Ready ~ Finish)를 확인하는 기능을 한다
import gamemode_2_gamemenu_statemachine as gamestatemachine

# ----- 게임 프레임워크 동작 함수들 -----

# 이벤트에 따른 동작 수행
def handle_events():

    events = get_events()

    for event in events:
        # SDL_QUIT일 경우 게임 종료
        if event.type == SDL_QUIT:
            game_framework.quit()

        # esc키 누를 경우 메인메뉴로 이동
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(gamemode_1_mainmenu)

        # 그 외
        else:
            # 플레이어 동작에 따른 이벤트 수행
            objects.player.handle_event(event)

def init():
    # 월드 초기 설정
    game_world.init_world()

    ### 테스트용
    print("### gamemenu 진입")
    print("### objects에 있는 오브젝트들")
    for layer in game_world.objects:
        for obj in layer:
            print(obj)

def finish():
    # 월드 있는 모든 오브젝트 지우기
    game_world.clear_objects()

    print("### gamemenu에서 나가기")
    pass

def update():
    # 월드 업데이트
    game_world.update_allobject()

def draw():
    clear_canvas()
    # 월드에 있는 모든 오브젝트 렌더링
    game_world.render_allobject()
    update_canvas()

def pause():
    # boy.wait_time = 10000000000000000000000
    pass

def resume():
    # boy.wait_time = get_time()
    pass


