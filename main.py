# ----------<main 파일>----------

from pico2d            import * # pico2d 모듈
from state_and_objects import * # 상태 및 동작들을 담은 모듈

# ----- world 전체 관련 -----

def handle_events():
    global gameplaying # 게임 실행중 여부

    events = get_events()

    # 입력받은 event에 따라
    for event in events:
        # SDL_QUIT 또는 Esc키 누를 시 게임 플레이 종료
        if event.type == SDL_QUIT:
            gameplaying = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            gameplaying = False
        # 그 외에는 플레이어의 handle_event에서 처리
        else:
            player.handle_event(event)

# world 초기 설정
def init_world():
    global gameplaying # 게임 실행중 여부
    global world # 오브젝트들을 담는 list
    global player # 플레이어

    gameplaying = True # 게임 실행을 True로 한다
    world = [] # list 초기화

    # 플레이어를 world에 추가한다
    player = Player()
    world.append(player)

# world 업데이트 <건드릴 필요 없음>
def update_world():
    for obj in world:
        obj.update()
    pass

# world 그리기 <건드릴 필요 없음>
def render_world():
    clear_canvas()
    for obj in world:
        obj.draw()
    update_canvas()

# ----- 실제 게임 실행 부분 -----

# 화면 실행
open_canvas()

# 초기 설정
init_world()

# 게임 진행
while gameplaying:

    handle_events() # event를 입력받는다
    update_world()  # world를 업데이트한다
    render_world()  # world를 그린다

    delay(0.01) # 동작 사이 지연 시간

# 게임 종료
close_canvas()
