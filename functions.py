# -----------<동작 함수들>-----------

# 이벤트 및 오브젝트별 동작 함수를 기록한 파일

from pico2d import * # pico2d 모듈 import
import objects       # 상태 머신 및 오브젝트 모듈 import

# ----- 이벤트 확인 함수 -----

### 임시 함수 (바로 다음 상태로 이동)
def func_temp(e):
    return True

# 스페이스 바 눌림
def space_down(e):
    return e[0] == "INPUT" and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

# ----- 각 오브젝트별 상세 동작 및 그리기 -----

# 플레이어 - 펀치 실행
def punch_activated(e):

    left_punch_keys = [
        SDLK_q, SDLK_w, SDLK_e, SDLK_r, SDLK_t,
        SDLK_a, SDLK_s, SDLK_d, SDLK_f, SDLK_g,
        SDLK_z, SDLK_x, SDLK_c, SDLK_v, SDLK_b
    ]
    right_punch_keys = [
        SDLK_i, SDLK_o, SDLK_p, SDLK_LEFTBRACKET, SDLK_RIGHTBRACKET,
        SDLK_j, SDLK_k, SDLK_l, SDLK_SEMICOLON, SDLK_QUOTE,
        SDLK_n, SDLK_m, SDLK_COMMA, SDLK_PERIOD, SDLK_SLASH
    ]

    # 펀치 쿨타임 (### 수치는 변경될 수 있음)
    PUNCH_COOLTIME = 50

    # 펀치 쿨타임이 0인 경우에만
    if objects.beattimer.punch_cooltime == 0:

        # 키가 눌렸다면
        if e[0] == "INPUT" and e[1].type == SDL_KEYDOWN:
            # 왼쪽 5줄 중 하나의 키를 눌렀다면 왼쪽 펀치
            if e[1].key in left_punch_keys:
                objects.player.nowpunchhand = "left"
                objects.state_machine.now_action = "punch"
                objects.beattimer.punch_cooltime = PUNCH_COOLTIME
                print("[<-] <왼쪽 펀치>")
                return True
            # 오른쪽 5줄 중 하나의 키를 눌렀다면 오른쪽 펀치
            elif e[1].key in right_punch_keys:
                objects.player.nowpunchhand = "right"
                objects.state_machine.now_action = "punch"
                objects.beattimer.punch_cooltime = PUNCH_COOLTIME

                print("[->] <오른쪽 펀치>")
                return True
            # 다른 키라면 어떤 방향 펀치도 아님
            else:
                objects.player.nowpunchhand = None
                print("펀치 아님")
                return False
    else:
        ### 테스트용
        print(f"펀치 쿨타임이 남아있습니다- {objects.beattimer.punch_cooltime}틱")

# 박자표 - 시간 업데이트 (1틱 간격)
def timeupdate(obj, nowstate):
    # nowtime 1틱씩 진행
    obj.nowtick += 1

    # 최대 틱(에서 100틱) 초과시 0틱으로 초기화
    if obj.nowtick > (obj.maxtick + 100):
        obj.nowtick = 0
    
    # 펀치중이라면
    if objects.state_machine.now_action == "punch":

        # 펀치 쿨타임 감소
        if objects.beattimer.punch_cooltime > 0:
            objects.beattimer.punch_cooltime -= 1
            
            # 쿨타임이 0이 되었다면
            if objects.beattimer.punch_cooltime <= 0:
                # 현재 하는 동작 없음
                objects.state_machine.now_action = None 

                ### 테스트용
                print(f"펀치 쿨타임 초기화 완료")
        else:
            pass

    ### 테스트용 - 박자 표시
    if obj.nowtick % obj.ticknum == 0 and obj.nowtick != 0:
        ### 큰 박자
        if obj.nowtick == obj.maxtick:
            ### print(f"<큰 박자> 박자표 [{obj.beatnum} / {obj.beatnum}] 박자")
            pass
        ### 그 외
        elif int(obj.nowtick / obj.ticknum) <= obj.beatnum:
            ### print(f"박자표 [{int(obj.nowtick / obj.ticknum)} / {obj.beatnum}] 박자")
            pass

# 배경 그리기
def draw_bg(obj):
    if obj.image == None:
        obj.image = load_image('img_background.png')

    obj.image.draw(400, 300, 800, 600)  # 배경 그리기

# 정보 그리기
def draw_state_info(nowstate):
    infoimg = None

    # 현재 상태에 따라 표시할 정보들
    # 별도 오브젝트가 아닌 것들

    if nowstate == "Ready":
        infoimg = load_image('img_ready_info_text.png')  # 왼쪽 글러브

        x, y = 400, 500          # x, y 위치
        SIZEX, SIZEY = 300, 60  # x, y 크기

        infoimg.draw(x, y, SIZEX, SIZEY)

    elif nowstate == "Standoff":
        pass

    elif nowstate == "Action":
        pass

# 글러브 그리기
def draw_glove(obj):

    if obj.image == None:
        # 글러브 방향에 따라 이미지 표시하기
        if obj.glovedir == "left":
            obj.image = load_image('img_glove_left.png')  # 왼쪽 글러브
        elif obj.glovedir == "right":
            obj.image = load_image('img_glove_right.png') # 오른쪽 글러브

    # 글러브 정보
    x, y = obj.x, obj.y   # x, y 위치
    SIZEX, SIZEY = 240, 240 # x, y 크기
    
    # 글러브 그리기
    obj.image.draw(x, y, SIZEX, SIZEY)

# 박자표 그리기
def draw_beattimer(obj):

    img_beat_bg     = load_image('img_beat_bg.png')     # 박자 배경
    img_beat_effect = load_image('img_beat_effect.png') # 현재 박자 이펙트
    img_beat_small  = load_image('img_beat_small.png')  # 작은 박자
    img_beat_big    = load_image('img_beat_big.png')    # 큰 박자

    beatnum = obj.beatnum  # 박자 수

    SIZE_BG_X, SIZE_BG_Y                 = 100, 100 # 박자표 틀 이미지 크기
    SIZE_EF_X, SIZE_EF_Y                 = 90, 90   # 박자표 효과 이미지 크기
    SIZE_BEAT_BIG_X, SIZE_BEAT_BIG_Y     = 70, 70   # 큰 박자 이미지 크기
    SIZE_BEAT_SMALL_X, SIZE_BEAT_SMALL_Y = 40, 40   # 작은 박자 이미지 크기

    CENTERX, CENTERY = 400, 500 # 박자표 중심

    # 박자표 이미지 list에서 - index는 list에서의 위치, beat는 실제 값
    for index, beatimg in enumerate(obj.beat_image_list):

        # 이미지 그리기 시작하는 위치
        startx = (CENTERX - (beatnum - 1) * SIZE_BG_X / 2) + (index * SIZE_BG_X)
        starty = CENTERY

        # 해당 박자가 없으면 - 그리기 종료
        if beatimg == None:
            break

        else:

            # 박자 배경 그리기
            img_beat_bg.draw(startx, starty, SIZE_BG_X, SIZE_BG_Y)

            # 박자 이펙트 그리기
            if index == (obj.nowtick // obj.ticknum - 1):
                img_beat_effect.draw(startx, starty, SIZE_EF_X, SIZE_EF_Y)

            # 해당 박자가 작은 박자이면 -
            if beatimg == "small":

                # 작은 박자 이미지 그리기
                img_beat_small.draw(startx, starty, SIZE_BEAT_SMALL_X, SIZE_BEAT_SMALL_Y)

            # 해당 박자가 큰 박자이면 - 큰 박자 이미지 그리기
            elif beatimg == "big":

                # 큰 박자 이미지 그리기
                img_beat_big.draw(startx, starty, SIZE_BEAT_BIG_X, SIZE_BEAT_BIG_Y)