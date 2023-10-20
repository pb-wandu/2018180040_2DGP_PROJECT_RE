# ----------<world 전체 관련 코드>----------

# world 전체 관련 내용을 기록한 파일

from objects import * # 상태 머신 및 오브젝트 모듈 import

# ----- world 전체 관련 코드 -----

objects = [ [ ], [ ] ]
# depth 0 : 배경
# depth 1 : 전면

img_bg = None # 배경 이미지

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

    # world 안에 오브젝트 추가
    # (해당 실물 오브젝트는 objects.py 끝부분에 있음)

    # 배경은 depth 0 (배경)에
    add_object(background, 0) # 배경

    # 나머지는 depth 1 (전면)에
    add_object(player, 1)    # 플레이어
    add_object(beattimer, 1) # 박자표

    ### 플레이어가 적보다 우선하는 등 추가 레이어 필요시 추가 예정

    pass

# -----<이 아래에 있는 코드는 건드릴 필요 없음>-----

# 단일 오브젝트 추가
def add_object(obj, depth):
    objects[depth].append(obj)

# 오브젝트들 추가
def add_objects(objs, depth):
    objects[depth] += objs

# 오브젝트 지우기
def remove_object(o):
    # objects에 있는 레이어에 대하여
    for layer in objects:
        # 레이어 안에 오브젝트가 있다면
        if obj in layer:
            print("지운 오브젝트 : " + str(type(obj)))
            # 해당 오브젝트를 지운다
            layer.remove(obj)
            return
    # 오류 발생시 오류 메시지 출력
    raise ValueError('존재하지 않는 object는 지울 수 없습니다')

# objects[] 안에 있는 오브젝트들 업데이트
def update_allobject():
    # world 안에 있는 모든 layer에 대하여
    for layer in objects:
        # layer 안에 있는 모든 오브젝트에 대하여
        for obj in layer:
            # 오브젝트 업데이트
            obj.update()

# objects[] 안에 있는 오브젝트들 그리기
def render_allobject():
    global img_bg

    # 화면 초기화
    clear_canvas()

    # world 안에 있는 모든 layer에 대하여
    for layer in objects:
        # layer 안에 있는 모든 오브젝트에 대하여
        for obj in layer:
            # 오브젝트 그리기
            obj.draw()

    # 화면 업데이트
    update_canvas()