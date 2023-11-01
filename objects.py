# ----------<상태 머신 및 오브젝트>----------

# 상태 머신 및 오브젝트들을 기록한 파일

from pico2d import *    # pico2d 모듈 import

# '모드 2 - 게임 메뉴'용 상태 머신 import
import gamemode_2_1_state as func_and_state
import objects


# ----- 배경 클래스 -----

class Background:
    image = None

    def update(self):
        pass

    def draw(self):
        func_and_state.state_machine.cur_state.draw(self)

# ----- 플레이어 클래스 -----

class Player:

    def __init__(self):
        self.nowpunchhand   = None # 현재 주먹을 지른 손
        self.ifpunchsuccess = None # 펀치 성공 여부
        pass

    @staticmethod
    def handle_event(event):
        # 입력받은 값에 따라 state_machine에서 event를 수행한다
        # e[0] = 이벤트 종류, e[1] = 실제 이벤트 값
        func_and_state.state_machine.handle_event(('INPUT', event))

    # update와 draw는 state_machine의 현재 상태에서
    # 그 클래스에 대한 실제 오브젝트의 동작을 수행한다

    @staticmethod
    def update():
        func_and_state.state_machine.cur_state.do(player)
        pass

    @staticmethod
    def draw():
        func_and_state.state_machine.cur_state.draw(player)
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

        self.punch_cooltime = 0 # 펀치 쿨타임

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
        func_and_state.state_machine.cur_state.do(beattimer)
        pass

    @staticmethod
    def draw():
        func_and_state.state_machine.cur_state.draw(beattimer)
        pass

# ----- 글러브 클래스 -----

class Glove:
    image = None    # 이미지
    glovedir = None # 글러브 방향
    x, y = 0, 0     # 글러브 위치

    ### (예정) 실제 제작할 때 내용 채워넣기

    def __init__(self, dir, posx, posy):

        # 입력값에 따른 방향 지정
        self.glovedir = dir
        # 입력값에 따른 위치 지정
        self.x, self.y = posx, posy
    
    # 글러브 위치 (재)지정
    def setpos(self, posx, posy):
        self.x, self.y = posx, posy

    @staticmethod
    def update():
        func_and_state.state_machine.cur_state.do(glove_l)
        func_and_state.state_machine.cur_state.do(glove_r)
        pass

    @staticmethod
    def draw():
        func_and_state.state_machine.cur_state.draw(glove_l)
        func_and_state.state_machine.cur_state.draw(glove_r)
        pass

# ----- 클래스별 실제 오브젝트 -----

# 플레이어 오브젝트
player = Player()

# 글러브 오브젝트
glove_l = Glove("left", 250, 80)
glove_r = Glove("right", 550, 80)

# 배경 오브젝트
background = Background()

# 박자표
# basicBeatTimer = BeatTimer(4, 50) # (4박자, 1박자당 50틱) 박자표 <기본>
# beattimer = basicBeatTimer # basicBeatTimer (기본 박자표)를 첫 박자표로 지정한다.

### 테스트용
beattimer = BeatTimer(3, 50)

### 추후 Finish 상태에서 exit했을 때 game_world.remove_object(o)를 이용하여 기존에 있는 박자표 오브젝트를 삭제하고
### 이어 Ready 상태에 enter시 새 박자표 오브젝트를 objects에 추가해야 한다.