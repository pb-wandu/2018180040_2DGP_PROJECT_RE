# ----------<상태 머신 및 오브젝트>----------

# 상태 머신 및 오브젝트들을 기록한 파일

from pico2d import *    # pico2d 모듈 import
from state import *     # 상태를 담은 모듈 import
from functions import * # 이벤트 및 오브젝트별 동작 모듈 import

# ----- 상태 머신 클래스 -----

class StateMachine:

    # 초기 상태 설정
    def __init__(self):
        self.cur_state = Ready # 초기 상태 : Ready 상태

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

# ----- 배경 클래스 -----

class Background:
    image = None

    def update(self):
        pass

    def draw(self):
        state_machine.cur_state.draw(self)

# ----- 플레이어 클래스 -----

class Player:
    def __init__(self):
        self.nowpunchhand = None # 현재 주먹을 지른 손
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
        state_machine.cur_state.draw(player)
        pass

    # 플레이어 - 펀치 날리기
    def punch_action(self):
        ### (예정) 펀치 이미지 추가
        ### punch = Punch(x위치, y위치)
        ### game_world.add_object(punch, 1)

        # 현재 펀치 날리는 손에 따른 구분
        if self.nowpunchhand == "left":
            # print("punch_action (left)")
            ### (예정) 실제 동작
            pass
        elif self.nowpunchhand == "right":
            # print("punch_action (right)")
            ### (예정) 실제 동작
            pass
        else:
            pass

# ----- 박자표 클래스 -----

class BeatTimer:

    # 박자표 이미지 list
    beat_image_list = [None, None, None, None, None, None]

    def __init__(self, bnum, ticknum):

        self.beatnum = bnum                   # 박자 수 (큰 박자 나오는 주기)
        self.nowtick = 0                      # 현재 틱수
        self.ticknum = ticknum                # 1박자당 틱수
        self.maxtick = ticknum * self.beatnum # 최대 틱수 (1박자당 ticknum틱)

        # '박자 수 - 1'개의 작은 박자와, 1개의 큰 박자를 넣는다
        for n in range(0, self.beatnum - 1):
            self.beat_image_list[n] = "small"
        self.beat_image_list[self.beatnum-1] = "big"

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
        state_machine.cur_state.draw(beattimer)
        pass


# 펀치 클래스
class Punch:
    image = None

    ### (예정) 실제 제작할 때 내용 채워넣기

    def __init__(self, posx, posy):
        # if Punch.image_l == None:
        #    Punch.image_l = load_image('펀치이미지왼쪽.png')
        # if Punch.image_r == None:
        #    Punch.image_r = load_image('펀치이미지오른쪽.png')
	    # 입력값에 따른 위치 지정
        self.x, self.y = posx, posy

    def draw(self):
	    # 펀치 이미지 그리기
        # self.image.draw(self.x, self.y)
        pass

    def update(self):
	    # 업데이트시 할 동작
        # if 조건:
            # 일정 시간이 지나면 펀치 오브젝트 삭제
        #    game_world.remove_object(self)
        pass

# ----- 클래스별 실제 오브젝트 -----

# 상태 머신 (world에 실물이 없는 가상 머신이다)
state_machine = StateMachine() # 상태 머신 오브젝트

# 플레이어 오브젝트
player = Player()

# 배경 오브젝트
background = Background()

# 박자표 종류
basicBeatTimer = BeatTimer(4, 100) # (4박자, 1박자당 100틱) 박자표 <기본>

# basicBeatTimer (기본 박자표)를 첫 박자표로 지정한다.
beattimer = basicBeatTimer

### 테스트용
beattimer = BeatTimer(5, 50)



### 추후 Finish 상태에서 exit했을 때 game_world.remove_object(o)를 이용하여 기존에 있는 박자표 오브젝트를 삭제하고
### 이어 Ready 상태에 enter시 새 박자표 오브젝트를 objects에 추가해야 한다.