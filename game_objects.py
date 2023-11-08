# ----------<오브젝트>----------

# 오브젝트들을 기록한 파일

from pico2d import *    # pico2d 모듈 import

# '모드 2 - 게임 메뉴'용 상태 머신 import
import gamemode_2_0_gamemenu                   # 게임 모드 gamemenu 모듈 import
import gamemode_2_1_state     as gamestate     # 상태 관련 모듈 import
import gamemode_2_1_functions as gamefunctions # 함수 모음 모듈 import

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

# ----- 게임 정보 클래스 -----

class Gameinfomation:
    img_info_hpbar_bg        = None
    img_info_hpbar_hp        = None
    img_info_hpbar_frame     = None
    img_info_playerlife      = None
    img_info_playerlife_lost = None

    img_whitesquare = None

    # 게임 정보 변수들
    p_nowlife = 0 # 현재 플레이어 하트
    p_maxlife = 0 # 최대 플레이어 하트
    e_nowhp   = 0 # 현재 적 체력
    e_maxhp   = 0 # 적 최대 체력

    def update(self):
        pass

    def draw(self):
        ### 상태 머신이 Ready상태가 아닐 경우 (임시)
        if gamestate.state_machine.cur_state != gamestate.Ready:
            # 하트 및 체력바 그리기
            gamefunctions.draw_life_hp_info(self,
                self.p_nowlife, self.p_maxlife, self.e_nowhp, self.e_maxhp)

            # 체력바 옆에 현재 체력/전체 체력 표시
            FONTSIZE = 20
            gamestate.font.draw(420, 470 - (10 + FONTSIZE // 2),
                                f'{self.e_nowhp} / {self.e_maxhp}', (0, 0, 0))

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

# 게임 정보
gameinfomation = Gameinfomation()

# 박자표

beattimer = BeatTimer(5, 30)

### 추후 Finish 상태에서 exit했을 때 game_world.remove_object(o)를 이용하여 기존에 있는 박자표 오브젝트를 삭제하고
### 이어 Ready 상태에 enter시 새 박자표 오브젝트를 objects에 추가해야 한다.