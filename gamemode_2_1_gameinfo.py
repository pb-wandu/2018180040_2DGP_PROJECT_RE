# ----------<'모드 2 - 게임 메뉴'용 게임 정보>----------

# 게임 정보들을 기록한 파일

from pico2d import *    # pico2d 모듈 import

import game_timer   # 타이머 모듈 import
import game_objects # 오브젝트 모듈 import

import gamemode_2_1_state     as gamestate     # 상태 관련 모듈 import
import gamemode_2_1_functions as gamefunctions # 함수 모음 모듈 import

# ----- 게임 정보 클래스 -----

class Gameinfomation:
    img_whitesquare = None

    # 대결 상대 체혁바
    img_info_hpbar_bg    = None
    img_info_hpbar_hp    = None
    img_info_hpbar_frame = None
    e_nowhp = 0 # 대결 상대 현재 체력
    e_maxhp = 0 # 대결 상대 최대 체력

    # 플레이어 하트
    img_info_playerlife      = None
    img_info_playerlife_lost = None
    p_nowlife = 0 # 현재 플레이어 하트
    p_maxlife = 0 # 최대 플레이어 하트

    nowtime = 0 # 시간 표시

    ### // 여기에다가 게임 점수(gamescore) 추가할 것

    def update(self):
        # 게임 시간 업데이트
        self.nowtime = get_time() - game_timer.gametimer.start_time
        pass

    def draw(self):

        ### 상태 머신이 Ready상태가 아닐 경우 (임시)
        if gamestate.state_machine.cur_state != gamestate.Ready:
            # 하트 및 체력바 그리기
            gamefunctions.draw_life_hp_info(self,
                self.p_nowlife, self.p_maxlife, self.e_nowhp, self.e_maxhp)

            # 체력바 옆에 현재 체력/전체 체력 표시
            FONTSIZE = 20
            game_objects.font.draw(420, 470 - (10 + FONTSIZE // 2),
                                f'{self.e_nowhp} / {self.e_maxhp}', (0, 0, 0))

        # 게임 시간 표시
        FONTSIZE = 24
        game_objects.font.draw(10, 600 - (10 + FONTSIZE // 2), f'(Time: {self.nowtime:.1f})', (0, 0, 0))