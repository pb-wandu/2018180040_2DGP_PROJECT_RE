# ----------<world 전체 관련 코드>----------

# world 전체 관련 코드를 기록한 파일

from objects import * # 상태 머신 및 동작들을 담은 모듈

# ----- world 전체 관련 코드 -----

# event 처리
def handle_events():
    global gameplaying # 게임 실행중 여부

    events = get_events() # event 입력받기

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
    pass

# world 초기 설정
def init_world():
    global gameplaying # 게임 실행중 여부
    global world # 오브젝트들을 담는 list

    gameplaying = True    # 게임 실행을 True로 한다
    state_machine.start() # 상태 머신을 실행시킨다

    # world 안에 있는 object들
    world = [
        player,   # 플레이어
        beattimer # 박자표
    ] 
    pass

# world 업데이트 <건드릴 필요 없음>
def update_world():
    # world 안에 있는 모든 오브젝트에 대하여
    for obj in world:
        # 오브젝트 업데이트
        obj.update()
    pass

# world 그리기 <건드릴 필요 없음>
def render_world():
    clear_canvas()
    # world 안에 있는 모든 오브젝트에 대하여
    for obj in world:
        # 오브젝트 그리기
        obj.draw()
    update_canvas()
    pass