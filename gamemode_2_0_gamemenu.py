# ----------<게임 프레임워크>----------

# 모드 2 - 게임 메뉴

# ----- 모듈 import -----

from pico2d import * # pico2d 모듈 import

import game_objects                     # 오브젝트 모듈 import
import game_playerAndEnemy      as PAE  # 플레이어 및 대결 상대 모듈 import
import game_PAE_ePatternAndWave as EPAW # 대결 상대 패턴 import

import game_world
import game_framework

import gamemode_1_0_mainmenu # 게임 모드 mainmenu 모듈 import

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
            game_framework.change_mode(gamemode_1_0_mainmenu)
            
        ### (테스트용) F1키 누를 경우 이전 wave로 이동
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F1:
            EPAW.move_prevWave()
            
        ### (테스트용) F2키 누를 경우 다음 wave로 이동
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F2:
            EPAW.move_nextWave()

        # 그 외
        else:
            # 플레이어 동작에 따른 이벤트 수행
            PAE.player.handle_event(event)

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
    pass

def resume():
    pass


