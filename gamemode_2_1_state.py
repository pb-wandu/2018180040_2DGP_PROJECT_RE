# ----------<'모드 2 - 게임 메뉴'용 상태>----------

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

from pico2d import *  # pico2d 모듈 import

import game_objects  # 오브젝트 모듈 import
import game_playerAndEnemy  # 플레이어 및 대결 상대 모듈 import

import gamemode_2_0_gamemenu  # 게임 모드 gamemenu 모듈 import
import gamemode_2_1_functions as functions  # 함수 모음 모듈 import

import game_timer  # 타이머 모듈 import

# 적 체력, 플레이어 하트
playerlife = 3
enemyhp = 100


# ----- gamemenu 각 상태별 동작 상세 클래스 -----

# Ready (준비 상태)
class Ready:

    # 상태 진입
    @staticmethod
    def enter():
        print("Ready (준비 상태) enter")

        # 준비 상태 진입시 게임 정보 기록
        game_objects.gameinfomation.e_maxhp = enemyhp
        game_objects.gameinfomation.e_nowhp = enemyhp
        game_objects.gameinfomation.p_maxlife = playerlife
        game_objects.gameinfomation.p_nowlife = playerlife

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
        if obj == game_playerAndEnemy.player:
            pass

        # 박자표
        elif obj == game_objects.beattimer:
            # Ready 상태에서는 박자표 시간 업데이트를 수행하지 않음
            pass

        pass

    # 현 상태에서 각 오브젝트 그리기
    @staticmethod
    def draw(obj):

        # 상태에 따른 정보 표시
        draw_state_info("Ready")

        # 배경
        if obj == game_objects.background_game:
            functions.draw_bg(obj)  # 배경 그리기
            pass

        # 플레이어
        elif obj == game_playerAndEnemy.player:
            pass

        # 글러브
        elif obj == game_playerAndEnemy.glove_l or obj == game_playerAndEnemy.glove_r:
            functions.draw_glove(obj)  # 글러브 그리기
            pass

        # 박자표
        elif obj == game_objects.beattimer:
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
        if obj == game_playerAndEnemy.player:
            pass

        # 박자표
        elif obj == game_objects.beattimer:
            functions.timeupdate(obj, "Standoff")  # 박자표 시간 업데이트
            pass

        pass

    # 현 상태에서 각 오브젝트 그리기
    @staticmethod
    def draw(obj):

        # 상태에 따른 정보 표시
        draw_state_info("Standoff")

        # 배경
        if obj == game_objects.background_game:
            functions.draw_bg(obj)  # 배경 그리기
            pass

        # 플레이어
        elif obj == game_playerAndEnemy.player:
            functions.draw_puncheffect(obj)  # 펀치 이펙트 그리기
            pass

        # 글러브
        elif obj == game_playerAndEnemy.glove_l or obj == game_playerAndEnemy.glove_r:
            functions.draw_glove(obj)  # 글러브 그리기
            pass

        # 박자표
        elif obj == game_objects.beattimer:
            functions.draw_beattimer(obj)  # 박자표 그리기
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
        if obj == game_playerAndEnemy.player:
            pass

        # 박자표
        elif obj == game_objects.beattimer:
            functions.timeupdate(obj, "Action")  # 박자표 시간 업데이트
            pass

        pass

    # 현 상태에서 각 오브젝트 그리기
    @staticmethod
    def draw(obj):

        # 배경
        if obj == game_objects.background_game:
            functions.draw_bg(obj)  # 배경 그리기
            pass

        # 플레이어
        elif obj == game_playerAndEnemy.player:
            functions.draw_puncheffect(obj)  # 펀치 이펙트 그리기
            pass

        # 글러브
        elif obj == game_playerAndEnemy.glove_l or obj == game_playerAndEnemy.glove_r:
            functions.draw_glove(obj)  # 글러브 그리기
            pass

        # 박자표
        elif obj == game_objects.beattimer:
            functions.draw_beattimer(obj)  # 박자표 그리기
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
    global nowstate

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

    # 펀치가 유효타로 들어간 타이밍
    HITTIMING = 8  # 앞뒤 타이밍 범위 (### 수치는 변경될 수 있음)
    hit_timing = (game_objects.beattimer.maxtick - HITTIMING,
                  game_objects.beattimer.maxtick + HITTIMING)

    # 펀치가 명중(크리티컬)으로 들어간 타이밍
    ### crit_timing = 더 좁은 범위 (예정)

    # 상태 머신이 Ready 상태가 아니고 펀치 쿨타임이 0인 경우에만
    if state_machine.cur_state != Ready and\
        game_objects.beattimer.punch_cooltime == 0:

        # 키가 눌렸다면
        if e[0] == "INPUT" and e[1].type == SDL_KEYDOWN:
            # 왼쪽 5줄 중 하나의 키를 눌렀다면 왼쪽 펀치
            if e[1].key in left_punch_keys:
                game_playerAndEnemy.player.nowpunchhand = "left"
                state_machine.now_action = "punch"
                game_objects.beattimer.punch_cooltime = PUNCH_COOLTIME

                functions.setglovespos()  # 글러브 위치 지정

                ### 테스트용
                print(f"[<-] <왼쪽 펀치> ({game_objects.beattimer.nowtick}틱)")
                print(f"맞힘 타이밍 : {hit_timing}")
                if hit_timing[0] <= game_objects.beattimer.nowtick <= hit_timing[1]:
                    game_playerAndEnemy.player.ifpunchsuccess = "hit"
                    print("공격 맞힘!")
                else:
                    game_playerAndEnemy.player.ifpunchsuccess = "failed"
                    print("공격 실패")

                return True

            # 오른쪽 5줄 중 하나의 키를 눌렀다면 오른쪽 펀치
            elif e[1].key in right_punch_keys:
                game_playerAndEnemy.player.nowpunchhand = "right"
                state_machine.now_action = "punch"
                game_objects.beattimer.punch_cooltime = PUNCH_COOLTIME

                functions.setglovespos()  # 글러브 위치 지정

                ### 테스트용
                print(f"[->] <오른쪽 펀치> ({game_objects.beattimer.nowtick}틱)")
                print(f"맞힘 타이밍 : {hit_timing}")
                if hit_timing[0] <= game_objects.beattimer.nowtick <= hit_timing[1]:
                    game_playerAndEnemy.player.ifpunchsuccess = "hit"
                    print("공격 맞힘!")
                else:
                    game_playerAndEnemy.player.ifpunchsuccess = "failed"
                    print("공격 실패")

                return True

            # 다른 키라면 어떤 방향 펀치도 아님
            else:
                game_playerAndEnemy.player.nowpunchhand = None

                ### 테스트용
                print("펀치 아님")

                return False
    else:
        ### 테스트용
        print(f"펀치 쿨타임이 남아있습니다- {game_objects.beattimer.punch_cooltime}틱")


# 상태에 따른 정보 그리기
def draw_state_info(nowstate):
    # 시간 표시
    FONTSIZE = 24
    nowtime = get_time() - game_timer.gametimer.start_time
    font.draw(10, 600 - (10 + FONTSIZE // 2), f'(Time: {nowtime:.1f})', (0, 0, 0))

    # 정보 이미지 표시
    infoimg = None

    ### 임시 정보
    e_nowhp, e_maxhp = 70, 100
    p_nowlife, p_maxlife = 2, 3

    # 현재 상태에 따라 표시할 정보들

    if nowstate == "Ready":
        infoimg = load_image('img_ready_info_text.png')

        x, y = 400, 500  # x, y 위치
        SIZEX, SIZEY = 300, 60  # x, y 크기

        infoimg.draw(x, y, SIZEX, SIZEY)

    elif nowstate == "Standoff":
        pass

    elif nowstate == "Action":
        pass


# ----- 상태 머신 클래스 -----

class StateMachine:

    # 초기 상태 설정
    def __init__(self):
        self.cur_state = Ready  # 초기 상태 : Ready 상태
        self.now_action = None  # 초기 상태 : 현재 동작 없음

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
                self.cur_state.exit()  # 현재 상태에서 exit
                self.cur_state = next_state  # 새로운 state 지정
                self.cur_state.enter()  # 새로운 상태로 enter
                return True
        return False

    # update와 draw는 state_machine의 현재 상태에서
    # 그 오브젝트에 대한 동작을 수행한다
    def update(self):
        self.cur_state.do(StateMachine)

    def draw(self):

        self.cur_state.draw(StateMachine)


# 상태 머신 (world에 실물이 없는 가상 머신이다)
state_machine = StateMachine()  # 상태 머신 오브젝트
