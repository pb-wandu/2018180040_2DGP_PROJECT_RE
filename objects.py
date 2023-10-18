# ----------<상태 머신 및 오브젝트>----------

# 상태 머신 및 오브젝트들을 기록한 파일

from pico2d import * # pico2d 모듈
from state import * # 상태를 담은 모듈

# ----- 상태 머신 클래스 -----

class StateMachine:

    # 초기 상태 설정
    def __init__(self):
        self.cur_state = Ready # 초기 상태 : Ready 상태

        # 동작 전환
        self.transitions = {
            Ready: {space_down: Standoff},
            Standoff: {temp: Standoff}
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

# ----- 플레이어 클래스 -----

class Player:
    def __init__(self):
        # self.x, self.y = 400, 90
        # self.sizex, self.sizey = 100, 100
        # self.image = load_image('image.png')
        pass

    @staticmethod
    def handle_event(event):
        # 입력받은 값에 따라 state_machine에서 event를 수행한다
        # e[0] = 이벤트 종류, e[1] = 실제 이벤트 값
        state_machine.handle_event(('INPUT', event))

    # update와 draw는 state_machine의 현재 상태에서
    # 그 오브젝트에 대한 동작을 수행한다

    @staticmethod
    def update():
        state_machine.cur_state.do(player)
        pass

    @staticmethod
    def draw():
        state_machine.cur_state.do(player)
        pass

# ----- 박자표 클래스 -----

class BeatTimer:
    def __init__(self):
        ### (테스트) 기본적으로 4/4박자를 기준으로 한다
        # 박자표에서의 현재 시간을 0으로 초기화
        self.nowtime = 0   # 현재 시간
        self.maxtime = 400 # 최대 시간

        # 100틱당 1박자
        self.ticktime = 0.25 / 100 # 1틱당 시간
        pass

    def handle_event(self, event):
        # 처리받을 입력이 없음
        pass

    # update와 draw는 state_machine의 현재 상태에서
    # 그 오브젝트에 대한 동작을 수행한다

    @staticmethod
    def update():
        state_machine.cur_state.do(beattimer)
        pass

    @staticmethod
    def draw():
        state_machine.cur_state.do(beattimer)
        pass

# ----- 클래스별 오브젝트 -----

# 상태 머신 (world에 실물이 없는 가상 머신이다)
state_machine = StateMachine() # 상태 머신 오브젝트

# 오브젝트 (world(게임 화면)에 실물이 있는 것들이다)
player        = Player()       # 플레이어 오브젝트
beattimer     = BeatTimer()    # 박자표 오브젝트
