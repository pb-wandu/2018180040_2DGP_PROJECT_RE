# ----------<world 전체 관련 코드>----------

# world 전체 관련 내용을 기록한 파일

from pico2d import *  # pico2d 모듈 import

import game_objects               # 오브젝트 모듈 import
import game_playerAndEnemy as pne # 플레이어 및 대결 상대 모듈 import

import gamemode_2_1_state    as gamestate # 상태 관련 모듈 import
import gamemode_2_1_gameinfo as gameinfo  # 게임 정보 모듈 import

import game_time # 시간 관련 모듈 import

import game_collisionCheck as collisionCheck # 게임 충돌 체크 import

# ----- world 전체 관련 코드 -----

objects = [ [ ], [ ], [ ] ] # object 전체를 담아두는 list
# depth 0 : 배경
# depth 1 : 전면

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
    global world # 오브젝트들을 담는 list

    # 상태 머신을 실행시킨다 (상태 머신은 gamemenu 모드에 해당)
    gamestate.state_machine.start()

    # gamestate.punch_cooltime = 0     # 펀치 쿨타임을 0으로 초기화
    game_objects.beattimer.nowtick = 0 # 박자표 틱을 0으로 초기화
    game_time.timer_setglovepos = 0    # 펀치위치 표시 타이머를 0으로 초기화

    gamestate.start_time = 0 # 시작 시간을 0으로 초기화

    # 폰트 지정
    FONTSIZE = 20
    game_objects.font = game_objects.load_font('FONT_KOTRA_HOPE_TTF.TTF', FONTSIZE)

    # world 안에 오브젝트 추가

    ### 추후 Finish 상태에서 exit했을 때 game_world.remove_object(o)를 이용하여 기존에 있는 박자표 오브젝트를 삭제하고
    ### 이어 Ready 상태에 enter시 새 박자표 오브젝트를 objects에 추가해야 한다.

    # 배경은 depth 0 (배경)에
    add_object(game_objects.background_game, 0) # 배경

    # 나머지는 depth 1 (전면)에
    add_object(game_objects.beattimer, 1) # 박자표
    add_object(pne.enemy, 1) # 대결 상대
    add_object(pne.player.glove_l, 1)  # 글러브 왼쪽
    add_object(pne.player.glove_r, 1)  # 글러브 오른쪽
    add_object(pne.player, 1) # 플레이어

    # 게임 정보는 depth 2 (가장 앞)에
    add_object(gameinfo.gameinfomation, 2)  # 게임 정보

    # 글러브와 대결 상대 충돌체크 지정
    collisionCheck.add_collision_pair('glove-enemy', pne.player.glove_l, None)
    collisionCheck.add_collision_pair('glove-enemy', pne.player.glove_r, None)
    collisionCheck.add_collision_pair('glove-enemy', None, pne.enemy)

    # 플레이어와 대결 상대 충돌체크 지정
    collisionCheck.add_collision_pair('player-enemy', pne.player, pne.enemy)

    pass

# -----<이 아래에 있는 코드는 건드릴 필요 없음>-----

# 단일 오브젝트 추가
def add_object(obj, depth):
    objects[depth].append(obj)

# 오브젝트들 추가
def add_objects(objs, depth):
    objects[depth] += objs

# 오브젝트 전부 정리
def clear_objects():
    for layer in objects:
        layer.clear()

# 오브젝트 지우기
def remove_object(obj):
    # objects에 있는 레이어에 대하여
    for layer in objects:
        # 레이어 안에 오브젝트가 있다면
        if obj in layer:
            print("지운 오브젝트 : " + str(type(obj)))

            # 해당 오브젝트를 월드에서 지운다
            layer.remove(obj)
            # 해당 오브젝트를 충돌 목록에서 지운다
            collisionCheck.remove_collision_object(o)
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

    # 충돌 처리
    collisionCheck.handle_collisions()

# objects[] 안에 있는 오브젝트들 그리기
def render_allobject():

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