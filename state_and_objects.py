# ----------<상태와 오브젝트>----------

from pico2d import * # pico2d 모듈
from state  import * # 상태를 담은 모듈

# ----- 이벤트 확인 함수들 -----

# 키 입력시
def keyinput(e, info, type_in, key_in):
    return e[0] == info and e[1].type == type_in and e[1].key == key_in

# a키 눌림 - 이건 임시로 둔 것
def a_down(e):
    keyinput(e, "INPUT", SDL_KEYDOWN, SDLK_a)

def temp(e):
    return False

# ----- 상태 머신 -----

class StateMachine:

    # 초기 상태 설정
    def __init__(self, player):
        self.player = player   # 플레이어 지정
        self.cur_state = Ready # 초기 상태 : Ready 상태

        # 동작 전환
        self.transitions = {
            Ready: {temp: Ready}
        }

    # 상태 머신 시작
    def start(self):
        self.cur_state.enter(self.player, ('NONE', 0))

    # 상태 머신 event 관리
    def handle_event(self, e):
        # event를 확인하고 현재 상태를 next_state로 지정한다
        for check_event, next_state in self.transitions[self.cur_state].items():
            # self.transitions{ }에 저장되어 있는대로
            if check_event(e):
                self.cur_state.exit(self.player, e)  # 현재 상태에서 exit
                self.cur_state = next_state          # 새로운 state 지정
                self.cur_state.enter(self.player, e) # 새로운 상태로 enter
                return True
        return False

    def update(self):
        # 각 오브젝트별 현재 상태에서의 do
        self.cur_state.do(self.player)

    def draw(self):
        # 각 오브젝트별 현재 상태에서의 draw
        self.cur_state.draw(self.player)

# ----- 플레이어 클래스 -----

class Player:
    def __init__(self):
        # self.x, self.y = 400, 90
        # self.sizex, self.sizey = 100, 100
        # self.image = load_image('image.png')

        # 플레이어 - 상태 머신
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        # e[0] = 이벤트 종류, e[1] = 실제 이벤트 값
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
