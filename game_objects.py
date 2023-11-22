# ----------<오브젝트>----------

# 오브젝트들을 기록한 파일

from pico2d import *    # pico2d 모듈 import

# '모드 2 - 게임 메뉴'용 상태 머신 import
import gamemode_2_1_state     as gamestate # 상태 관련 모듈 import
import gamemode_2_1_gameinfo  as gameinfo  # 게임 정보 모듈 import

import game_playerAndEnemy as PAE # 플레이어 및 대결 상대 모듈 import

import game_time # 시간 관련 모듈 import

# ----- 배경 클래스 -----

class Background_main:
    image = None

    def update(self):
        pass

    def draw(self):
        gamestate.state_machine.cur_state.draw(self)

    pass

class Background_game:
    image = None

    def update(self):
        pass

    def draw(self):
        gamestate.state_machine.cur_state.draw(self)

# ----- 박자표 클래스 -----

class BeatTimer:
    img_beat_bg = None
    img_beat_effect = None
    img_beat_small = None
    img_beat_big = None

    # 박자표 이미지 list
    beat_image_list = [None, None, None, None, None, None]

    def __init__(self, bnum, ticknum):

        self.beatnum = bnum                   # 박자 수 (큰 박자 나오는 주기)
        self.nowtick = 0                      # 현재 틱수
        self.ticknum = ticknum                # 1박자당 틱수
        self.maxtick = ticknum * self.beatnum # 최대 틱수 (1박자당 ticknum틱)

        self.punch_cooltime = 0 # 펀치 쿨타임

        pass

    # 박자 설정 (임시 지정)
    def set_beats(self, beats):

        num = 0
        for beat in beats:
            if beat != None:
                self.beat_image_list[num] = beat
                num += 1
        pass

    def handle_event(self, event):
        # 처리받을 입력이 없음
        pass

    # update와 draw는 state_machine의 현재 상태에서
    # 그 클래스에 대한 실제 오브젝트의 동작을 수행한다

    @staticmethod
    def update():
        gamestate.state_machine.cur_state.do(beattimer)
        pass

    @staticmethod
    def draw():
        gamestate.state_machine.cur_state.draw(beattimer)
        pass

# ----- 클래스별 실제 오브젝트 -----

# 배경 오브젝트
background_main = Background_main() # 메인메뉴 배경
background_game = Background_game() # 게임메뉴 배경

# 박자표
beattimer = BeatTimer(4, 40)
beattimer.set_beats(PAE.enemy.patternlist[PAE.enemy.nowPattern])

### 추후 Finish 상태에서 exit했을 때 game_world.remove_object(o)를 이용하여 기존에 있는 박자표 오브젝트를 삭제하고
### 이어 Ready 상태에 enter시 새 박자표 오브젝트를 objects에 추가해야 한다.