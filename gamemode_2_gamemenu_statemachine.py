# ----------<'모드 2 - 게임 메뉴'용 상태 머신>----------

# ----- 게임 흐름 -----

### (예정) Main (게임 메인 화면) 만들기

# (첫 시작, 또는 새로운 스테이지 진입)
# Ready        : 준비 상태

# (3개 단계를 반복)
# Standoff     : 대치 상태
# Action       : 동작
# ActionResult : 동작 결과

# (적의 HP가 0 이하가 되면)
# Finish       : 대결 완료

# ----- 모듈 import -----

from pico2d import *    # pico2d 모듈 import
import objects          # 상태 머신 및 오브젝트 모듈 import

import gamemode_2_gamemenu # 게임 모드 gamemenu 모듈 import

# import game_world
# import game_framework
# import gamemode_1_mainmenu # 게임 모드 mainmenu 모듈 import

# ----- gamemenu 각 상태별 동작 상세 클래스 -----

# Ready (준비 상태)
class Ready:

    # 상태 진입
    @staticmethod
    def enter():
        print("Ready (준비 상태) enter")
        pass

    # 상태 종료
    @staticmethod
    def exit():
        print("Ready (준비 상태) exit")
        pass

    # 현 상태에서 각 오브젝트에 따른 동작
    @staticmethod
    def do(obj):

        # 플레이어
        if obj == objects.player:
            pass

        # 박자표
        elif obj == objects.beattimer:
            # Ready 상태에서는 박자표 시간 업데이트를 수행하지 않음
            pass

        pass

    # 현 상태에서 각 오브젝트 그리기
    @staticmethod
    def draw(obj):

        # 상태에 따른 정보 표시
        draw_state_info("Ready")

        # 배경
        if obj == objects.background:
            draw_bg(obj)  # 배경 그리기
            pass

        # 플레이어
        elif obj == objects.player:
            pass

        # 글러브
        elif obj == objects.glove_l or obj == objects.glove_r:
            draw_glove(obj) # 글러브 그리기
            pass

        # 박자표
        elif obj == objects.beattimer:
            # Ready 상태에서는 박자표를 그리지 않음
            pass

        pass

# Standoff (대치 상태)
class Standoff:
    # 상태 진입
    @staticmethod
    def enter():
        print("Standoff (대치 상태) enter")
        pass

    # 상태 종료
    @staticmethod
    def exit():
        print("Standoff (대치 상태) exit")
        pass

    # 현 상태에서 각 오브젝트에 따른 동작
    @staticmethod
    def do(obj):

        # 플레이어
        if obj == objects.player:
            pass

        # 박자표
        elif obj == objects.beattimer:
            timeupdate(obj, "Standoff") # 박자표 시간 업데이트
            pass

        pass

    # 현 상태에서 각 오브젝트 그리기
    @staticmethod
    def draw(obj):

        # 상태에 따른 정보 표시
        draw_state_info("Standoff")

        # 배경
        if obj == objects.background:
            draw_bg(obj) # 배경 그리기
            pass

        # 플레이어
        elif obj == objects.player:
            pass

        # 글러브
        elif obj == objects.glove_l or obj == objects.glove_r:
            draw_glove(obj) # 글러브 그리기
            pass

        # 박자표
        elif obj == objects.beattimer:
            draw_beattimer(obj) # 박자표 그리기
            pass

        pass

# Action (동작)
class Action:
    @staticmethod
    def enter():
        print("Action (동작 상태) enter")
        pass

    # 상태 종료
    @staticmethod
    def exit():

        print("Action (동작 상태) exit")
        pass

    # 현 상태에서 각 오브젝트에 따른 동작
    @staticmethod
    def do(obj):

        # 상태에 따른 정보 표시
        draw_state_info("Action")

        # 플레이어
        if obj == objects.player:
            pass

        # 박자표
        elif obj == objects.beattimer:
            timeupdate(obj, "Action") # 박자표 시간 업데이트
            pass

        pass

    # 현 상태에서 각 오브젝트 그리기
    @staticmethod
    def draw(obj):

        # 배경
        if obj == objects.background:
            draw_bg(obj) # 배경 그리기
            pass

        # 플레이어
        elif obj == objects.player:
            pass

        # 글러브
        elif obj == objects.glove_l or obj == objects.glove_r:
            draw_glove(obj) # 글러브 그리기
            pass

        # 박자표
        elif obj == objects.beattimer:
            draw_beattimer(obj) # 박자표 그리기
            pass

        pass

# ActionResult (동작 결과)
class ActionResult:
    @staticmethod
    def enter():
        pass

    @staticmethod
    def exit():
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass

# Finish (대결 완료)
class Finish:
    @staticmethod
    def enter():
        pass

    @staticmethod
    def exit():
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass

# ----- 상태 머신 함수들 -----

### 임시 함수 (바로 다음 상태로 이동)
def func_temp(e):
    return True

# 스페이스 바 눌림
def space_down(e):
    return e[0] == "INPUT" and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

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
    PUNCH_COOLTIME = 20

    # 펀치가 유효타로 들어간 타이밍
    HITTIMING = 8 # 앞뒤 타이밍 범위 (### 수치는 변경될 수 있음)
    hit_timing = (objects.beattimer.maxtick - HITTIMING,
                  objects.beattimer.maxtick + HITTIMING)

    # 펀치가 명중(크리티컬)으로 들어간 타이밍
    ### crit_timing = 더 좁은 범위 (예정)

    # 펀치 쿨타임이 0인 경우에만
    if objects.beattimer.punch_cooltime == 0:

        # 키가 눌렸다면
        if e[0] == "INPUT" and e[1].type == SDL_KEYDOWN:
            # 왼쪽 5줄 중 하나의 키를 눌렀다면 왼쪽 펀치
            if e[1].key in left_punch_keys:
                objects.player.nowpunchhand = "left"
                state_machine.now_action = "punch"
                objects.beattimer.punch_cooltime = PUNCH_COOLTIME

                setglovespos() # 글러브 위치 지정
                
                ### 테스트용
                print(f"[<-] <왼쪽 펀치> ({objects.beattimer.nowtick}틱)")
                print(f"맞힘 타이밍 : {hit_timing}")
                if hit_timing[0] <= objects.beattimer.nowtick <= hit_timing[1]:
                    print("공격 맞힘!")
                else:
                    print("공격 실패")

                return True

            # 오른쪽 5줄 중 하나의 키를 눌렀다면 오른쪽 펀치
            elif e[1].key in right_punch_keys:
                objects.player.nowpunchhand = "right"
                state_machine.now_action = "punch"
                objects.beattimer.punch_cooltime = PUNCH_COOLTIME

                setglovespos()  # 글러브 위치 지정

                ### 테스트용
                print(f"[->] <오른쪽 펀치> ({objects.beattimer.nowtick}틱)")
                print(f"맞힘 타이밍 : {hit_timing}")
                if hit_timing[0] <= objects.beattimer.nowtick <= hit_timing[1]:
                    print("공격 맞힘!")
                else:
                    print("공격 실패")

                return True

            # 다른 키라면 어떤 방향 펀치도 아님
            else:
                objects.player.nowpunchhand = None

                ### 테스트용
                print("펀치 아님")

                return False
    else:
        ### 테스트용
        print(f"펀치 쿨타임이 남아있습니다- {objects.beattimer.punch_cooltime}틱")

# 글러브 - 펀치 동작에 따른 위치설정
def setglovespos():

    if objects.player.nowpunchhand == None:
        objects.glove_l.setpos(250, 80)
        objects.glove_r.setpos(550, 80)

    elif objects.player.nowpunchhand == "left":
        objects.glove_l.setpos(250+100, 80+120)
        objects.glove_r.setpos(550, 80)

    elif objects.player.nowpunchhand == "right":
        objects.glove_l.setpos(250, 80)
        objects.glove_r.setpos(550-100, 80+120)

# 박자표 - 시간 업데이트 (1틱 간격)
def timeupdate(obj, nowstate):
    global timer_setglovepos

    # 왼손 또는 오른손 펀치를 날리고 있자면
    if objects.player.nowpunchhand == "left" or objects.player.nowpunchhand == "right":
        timer_setglovepos += 1
        # 펀치를 날린지 일정 시간이 지나면 펀치중인 손을 없음으로 초기화
        if timer_setglovepos >= 30:
            objects.player.nowpunchhand = None
            timer_setglovepos = 0
            setglovespos() # 글러브 위치설정

    # nowtime 1틱씩 진행
    obj.nowtick += 1

    # 해당 오브젝트의 박자 수에서 1박자가 더 넘어가면 0틱으로 초기화
    nextbeattick = obj.maxtick * ((obj.beatnum + 1) / obj.beatnum)
    if obj.nowtick > nextbeattick:
        obj.nowtick = 0

    # 펀치중이라면
    if state_machine.now_action == "punch":

        # 펀치 쿨타임 감소
        if objects.beattimer.punch_cooltime > 0:
            objects.beattimer.punch_cooltime -= 1

            # 쿨타임이 0이 되었다면
            if objects.beattimer.punch_cooltime <= 0:
                # 현재 하는 동작 없음
                state_machine.now_action = None

                ### 테스트용
                print(f"펀치 쿨타임 초기화 완료")
        else:
            pass

    ### 테스트용 - 박자 표시
    if obj.nowtick % obj.ticknum == 0 and obj.nowtick != 0:
        ### 큰 박자
        if obj.nowtick == obj.maxtick:
            print(f"<큰 박자> 박자표 [{obj.beatnum} / {obj.beatnum}] 박자")
            pass
        ### 그 외
        elif int(obj.nowtick / obj.ticknum) <= obj.beatnum:
            print(f"박자표 [{int(obj.nowtick / obj.ticknum)} / {obj.beatnum}] 박자")
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

        x, y = 400, 500  # x, y 위치
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
            obj.image = load_image('img_glove_right.png')  # 오른쪽 글러브

    # 글러브 정보
    x, y = obj.x, obj.y  # x, y 위치
    SIZEX, SIZEY = 240, 240  # x, y 크기

    # 글러브 그리기
    obj.image.draw(x, y, SIZEX, SIZEY)


# 박자표 그리기
def draw_beattimer(obj):
    img_beat_bg = load_image('img_beat_bg.png')  # 박자 배경
    img_beat_effect = load_image('img_beat_effect.png')  # 현재 박자 이펙트
    img_beat_small = load_image('img_beat_small.png')  # 작은 박자
    img_beat_big = load_image('img_beat_big.png')  # 큰 박자

    beatnum = obj.beatnum  # 박자 수

    SIZE_BG_X, SIZE_BG_Y = 100, 100  # 박자표 틀 이미지 크기
    SIZE_EF_X, SIZE_EF_Y = 90, 90  # 박자표 효과 이미지 크기
    SIZE_BEAT_BIG_X, SIZE_BEAT_BIG_Y = 70, 70  # 큰 박자 이미지 크기
    SIZE_BEAT_SMALL_X, SIZE_BEAT_SMALL_Y = 40, 40  # 작은 박자 이미지 크기

    CENTERX, CENTERY = 400, 500  # 박자표 중심

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

# ----- 상태 머신 클래스 -----

class StateMachine:

    # 초기 상태 설정
    def __init__(self):
        self.cur_state = Ready # 초기 상태 : Ready 상태
        self.now_action = None # 초기 상태 : 현재 동작 없음

        # 동작 전환
        self.transitions = {
            Ready: {space_down: Standoff},
            Standoff: {punch_activated: Action},
            Action: {func_temp: Standoff}
        }

    # 상태 머신 시작
    def start(self):
        self.cur_state.enter()

    # 상태 머신 event 관리
    def handle_event(self, e):
        # event를 확인하고 현재 상태를 next_state로 지정한다
        for check_event, next_state in self.transitions[self.cur_state].items():
            # self.transitions{ }에 저장되어 있는대로
            if check_event(e):
                self.cur_state.exit()       # 현재 상태에서 exit
                self.cur_state = next_state # 새로운 state 지정
                self.cur_state.enter()      # 새로운 상태로 enter
                return True
        return False

    # update와 draw는 state_machine의 현재 상태에서
    # 그 오브젝트에 대한 동작을 수행한다
    # (참고 : 상태 머신 자체는 update하거나 draw할 내용 없음)

    def update(self):
        self.cur_state.do(StateMachine)

    def draw(self):
        self.cur_state.draw(StateMachine)

# 상태 머신 (world에 실물이 없는 가상 머신이다)
state_machine = StateMachine() # 상태 머신 오브젝트

