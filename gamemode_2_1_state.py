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

import game_objects               # 오브젝트 모듈 import
import game_playerAndEnemy as PAE # 플레이어 및 대결 상대 모듈 import

import gamemode_2_0_gamemenu as gamemenu # 게임 모드 gamemenu 모듈 import
import gamemode_2_1_gameinfo as gameinfo # 게임 정보 관련 모듈 import

import game_time # 시간 관련 모듈 import

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
        gameinfo.gameinfomation.e_maxhp = enemyhp
        gameinfo.gameinfomation.e_nowhp = enemyhp
        gameinfo.gameinfomation.p_maxlife = playerlife
        gameinfo.gameinfomation.p_nowlife = playerlife

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
        if obj == PAE.player:
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
            gameinfo.draw_bg(obj)  # 배경 그리기
            pass

        # 플레이어
        elif obj == PAE.player:
            pass

        # 글러브
        elif obj == PAE.player.glove_l or obj == PAE.player.glove_r:
            PAE.draw_glove(obj)  # 글러브 그리기
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
        if obj == PAE.player:
            pass

        # 박자표
        elif obj == game_objects.beattimer:
            game_time.timeupdate(obj, "Standoff")  # 박자표 시간 업데이트
            pass

        pass

    # 현 상태에서 각 오브젝트 그리기
    @staticmethod
    def draw(obj):

        # 상태에 따른 정보 표시
        draw_state_info("Standoff")

        # 배경
        if obj == game_objects.background_game:
            gameinfo.draw_bg(obj)  # 배경 그리기
            pass

        # 플레이어
        elif obj == PAE.player:
            PAE.draw_puncheffect(obj)  # 펀치 이펙트 그리기
            pass

        # 글러브
        elif obj == PAE.player.glove_l or obj == PAE.player.glove_r:
            PAE.draw_glove(obj)  # 글러브 그리기
            pass

        # 박자표
        elif obj == game_objects.beattimer:
            gameinfo.draw_beattimer(obj)  # 박자표 그리기
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
        if obj == PAE.player:
            pass

        # 박자표
        elif obj == game_objects.beattimer:
            game_time.timeupdate(obj, "Action")  # 박자표 시간 업데이트
            pass

        pass

    # 현 상태에서 각 오브젝트 그리기
    @staticmethod
    def draw(obj):

        # 배경
        if obj == game_objects.background_game:
            gameinfo.draw_bg(obj)  # 배경 그리기
            pass

        # 플레이어
        elif obj == PAE.player:
            PAE.draw_puncheffect(obj)  # 펀치 이펙트 그리기
            pass

        # 글러브
        elif obj == PAE.player.glove_l or obj == PAE.player.glove_r:
            PAE.draw_glove(obj)  # 글러브 그리기
            pass

        # 박자표
        elif obj == game_objects.beattimer:
            gameinfo.draw_beattimer(obj)  # 박자표 그리기
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
    global combochanged # 콤보 바뀜 여부
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

    # 펀치가 유효타로 들어간 타이밍 (### 수치는 변경될 수 있음)
    CRITTIMING = 4  # 명중(크리티컬)  앞뒤 타이밍 범위
    HITTIMING  = 12 # 맞힘(일반 히트) 앞뒤 타이밍 범위

    # 상태 머신이 Ready 상태가 아니고 펀치 쿨타임이 0인 경우에만
    if state_machine.cur_state != Ready and\
        game_objects.beattimer.punch_cooltime == 0:

        # 키가 눌렸다면
        if e[0] == "INPUT" and e[1].type == SDL_KEYDOWN:
            # 왼쪽 5줄 중 하나의 키를 눌렀다면 왼쪽 펀치
            if e[1].key in left_punch_keys:
                PAE.player.nowpunchhand = "left"
                state_machine.now_action = "punch"
                game_objects.beattimer.punch_cooltime = PUNCH_COOLTIME

                PAE.setglovespos()  # 글러브 위치 지정

                ### 테스트용

                imglist = game_objects.beattimer.beat_image_list # 박자 이미지 리스트
                hittime = game_objects.beattimer.nowtick # 펀치를 누른 시간
                hitbeat = int(hittime / game_objects.beattimer.ticknum) # 펀치를 누른 현재 박자

                print(f"[<-] <왼쪽 펀치> ({hittime}틱)")
                print(f"### {hitbeat}번째 박자에서 클릭")

                # 큰 박자
                if imglist[hitbeat-1] == "big":

                    # 치명타
                    if (hitbeat * game_objects.beattimer.ticknum - CRITTIMING <= hittime
                         <= hitbeat * game_objects.beattimer.ticknum + CRITTIMING):
                        PAE.player.ifpunchsuccess = "crit"

                        # 콤보 수 증가
                        gameinfo.gameinfomation.nowcombo += 1

                        print("!!공격 명중!!")

                    # 명중
                    elif (hitbeat * game_objects.beattimer.ticknum - HITTIMING <= hittime
                         <= hitbeat * game_objects.beattimer.ticknum + HITTIMING):
                        PAE.player.ifpunchsuccess = "hit"

                        # 콤보 수 증가
                        gameinfo.gameinfomation.nowcombo += 1

                        print("공격 맞힘!")

                    # 놓침
                    else:
                        PAE.player.ifpunchsuccess = "failed"
                        # 콤보 수 초기화
                        gameinfo.gameinfomation.nowcombo = 0
                        print("공격 놓침...")

                # 작은 박자
                else:
                    PAE.player.ifpunchsuccess = "failed"
                    # 콤보 수 초기화
                    gameinfo.gameinfomation.nowcombo = 0
                    print("공격 실패...")

                return True

            # 오른쪽 5줄 중 하나의 키를 눌렀다면 오른쪽 펀치
            elif e[1].key in right_punch_keys:
                PAE.player.nowpunchhand = "right"
                state_machine.now_action = "punch"
                game_objects.beattimer.punch_cooltime = PUNCH_COOLTIME

                PAE.setglovespos()  # 글러브 위치 지정

                ### 테스트용

                imglist = game_objects.beattimer.beat_image_list # 박자 이미지 리스트
                hittime = game_objects.beattimer.nowtick # 펀치를 누른 시간
                hitbeat = int(hittime / game_objects.beattimer.ticknum) # 펀치를 누른 현재 박자

                print(f"[->] <오른쪽 펀치> ({hittime}틱)")
                print(f"### {hitbeat}번째 박자에서 클릭")

                # 큰 박자
                if imglist[hitbeat-1] == "big":

                    if (hitbeat * game_objects.beattimer.ticknum - CRITTIMING <= hittime
                         <= hitbeat * game_objects.beattimer.ticknum + CRITTIMING):
                        PAE.player.ifpunchsuccess = "crit"

                        # 콤보 수 증가
                        gameinfo.gameinfomation.nowcombo += 1

                        print("!!공격 명중!!")

                    elif (hitbeat * game_objects.beattimer.ticknum - HITTIMING <= hittime
                         <= hitbeat * game_objects.beattimer.ticknum + HITTIMING):
                        PAE.player.ifpunchsuccess = "hit"

                        # 콤보 수 증가
                        gameinfo.gameinfomation.nowcombo += 1

                        print("공격 맞힘!")

                    # 놓침
                    else:
                        PAE.player.ifpunchsuccess = "failed"
                        # 콤보 수 초기화
                        gameinfo.gameinfomation.nowcombo = 0
                        print("공격 놓침...")

                # 작은 박자
                else:
                    PAE.player.ifpunchsuccess = "failed"
                    # 콤보 수 초기화
                    gameinfo.gameinfomation.nowcombo = 0
                    print("공격 실패...")

                return True

            # 다른 키라면 어떤 방향 펀치도 아님
            else:
                PAE.player.nowpunchhand = None

                ### 테스트용
                print("펀치 아님")

                return False
    else:
        ### 테스트용
        print(f"펀치 쿨타임이 남아있습니다- {game_objects.beattimer.punch_cooltime}틱")


# 상태에 따른 정보 그리기
def draw_state_info(nowstate):

    # 정보 이미지 표시
    infoimg = None

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

