# ----------<world 전체 관련 코드>----------

# world 전체 관련 코드를 기록한 파일

from statemachine_and_objects import * # 상태 머신 및 동작들을 담은 모듈

# ----- world 전체 관련 코드 -----

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