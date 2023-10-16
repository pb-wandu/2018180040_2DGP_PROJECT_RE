# ----------<상태와 오브젝트>----------

from pico2d import * # pico2d 모듈
from state  import * # 상태를 담은 모듈

# ----- 이벤트 확인 함수들 -----

# 키 입력
def keyinput(e, info, type, key):
    return e[0] == info and e[1].type == type and e[1].key == key

# a키 눌림
def a_down(e):
    keyinput(e, "INPUT", SDL_KEYDOWN, SDLK_a)

# ----- 플레이어 상태 머신 -----

class StateMachine:

    # 초기 상태로
    def __init__(self, player):
        self.player = player
        self.cur_state = Idle

        # '플레이어' 동작 전환
        self.transitions = {
            Idle: {a_down: Idle}
        }

    def start(self):
        self.cur_state.enter(self.player, ('NONE', 0))

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True
        return False

    def update(self):
        self.cur_state.do(self.player)

    def draw(self):
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
