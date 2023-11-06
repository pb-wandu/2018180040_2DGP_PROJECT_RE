# ----------<플레이어, 대결 상대>----------

# 플레이어, 대결 상대를 기록한 파일

from pico2d import *    # pico2d 모듈 import

# '모드 2 - 게임 메뉴'용 상태 머신 import
import gamemode_2_0_gamemenu                   # 게임 모드 gamemenu 모듈 import
import gamemode_2_1_state     as gamestate     # 상태 관련 모듈 import
import gamemode_2_1_functions as gamefunctions # 함수 모음 모듈 import

# ----- 플레이어 클래스 -----

class Player:

    def __init__(self):
        self.nowpunchhand = None  # 현재 주먹을 지른 손
        self.ifpunchsuccess = None  # 펀치 성공 여부
        pass

    @staticmethod
    def handle_event(event):
        # 입력받은 값에 따라 state_machine에서 event를 수행한다
        # e[0] = 이벤트 종류, e[1] = 실제 이벤트 값
        gamestate.state_machine.handle_event(('INPUT', event))

    # update와 draw는 state_machine의 현재 상태에서
    # 그 클래스에 대한 실제 오브젝트의 동작을 수행한다

    @staticmethod
    def update():
        gamestate.state_machine.cur_state.do(player)
        pass

    @staticmethod
    def draw():
        gamestate.state_machine.cur_state.draw(player)
        pass


# ----- 적 클래스 -----

class Enemy:

    def __init__(self):
        ### 내용 추가할 것 있으면 추가 예정
        pass

    def handle_event(self, event):
        # 처리받을 입력이 없음
        pass

    # update와 draw는 state_machine의 현재 상태에서
    # 그 클래스에 대한 실제 오브젝트의 동작을 수행한다

    @staticmethod
    def update():
        gamestate.state_machine.cur_state.do(enemy)
        pass

    @staticmethod
    def draw():
        gamestate.state_machine.cur_state.draw(enemy)
        pass

# ----- 클래스별 실제 오브젝트 -----

player = Player() # 플레이어 오브젝트
enemy = Enemy()   # 대결 상대 오브젝트