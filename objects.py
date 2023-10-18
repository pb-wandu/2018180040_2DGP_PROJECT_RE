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
    # 그 클래스에 대한 실제 오브젝트의 동작을 수행한다

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
    def __init__(self, bnum, ctime):
        ### (테스트) 기본적으로 4/4박자를 기준으로 한다
        # 박자표에서의 현재 틱수를 0으로 초기화
        self.beatnum = bnum                             # 박자수 (큰 박자 나오는 주기)
        self.cycle_time = ctime                         # 큰 박자 사이의 '실제 시간'
        self.nowtick = 0                                # 현재 틱수
        self.maxtick = 100 * self.beatnum               # 최대 틱수 (1박당 100틱)
        self.beat1time = self.cycle_time / self.beatnum # 한 박자당 시간
        self.tick1time = self.beat1time / 100           # 1틱당 시간

        pass

    def handle_event(self, event):
        # 처리받을 입력이 없음
        pass

    # update와 draw는 state_machine의 현재 상태에서
    # 그 클래스에 대한 실제 오브젝트의 동작을 수행한다

    @staticmethod
    def update():
        state_machine.cur_state.do(beattimer)
        pass

    @staticmethod
    def draw():
        state_machine.cur_state.do(beattimer)
        pass

# ----- 클래스별 실제 오브젝트 -----

# 상태 머신 (world에 실물이 없는 가상 머신이다)
state_machine = StateMachine() # 상태 머신 오브젝트

# 오브젝트 (world(게임 화면)에 실물이 있는 것들이다)

# 플레이어 오브젝트 : 플레이어는 고정된 하나의 오브젝트임이 명확하다.
player = Player()

# 하지만 박자표는? 박자표는 등장 적에 따라 바뀌는 오브젝트이다.
# 박자표 오브젝트의 초기화 원본은 'def __init__(self, bnum, ctime):' 이다
# bnum은 박자 수를, ctime은 박자가 1바퀴 돌 때의 실제 소요 시간을 말한다.
# basicBeatTimer (기본 박자표)를 첫 박자표로 지정해준다.

# 박자표 종류
basicBeatTimer = BeatTimer(4, 1.0) # 박자표 (1초에 4박자) <기본>
### secondBeatTimer = BeatTimer(5, 1.4) # 박자표 (1.4초에 5박자) <- 예시입니다

# 첫 박자표는 기본 박자표 (1초에 4박자)로 지정한다.
beattimer = basicBeatTimer

### 추후 Finish 상태에서 exit했을 때 game_world.remove_object(o)를 이용하여 기존에 있는 박자표 오브젝트를 삭제하고
### 이어 Ready 상태에 enter시 새 박자표 오브젝트를 objects에 추가해야 한다.