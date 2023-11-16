# ----------<'모드 2 - 게임 메뉴'용 게임 정보>----------

# 게임 정보들을 기록한 파일

from pico2d import *    # pico2d 모듈 import

import game_timer   # 타이머 모듈 import
import game_objects # 오브젝트 모듈 import

import gamemode_2_1_state     as gamestate     # 상태 관련 모듈 import
import gamemode_2_1_functions as gamefunctions # 함수 모음 모듈 import

# ----- 게임 정보 클래스 -----

class Gameinfomation:

    def __init__(self):

        self.img_whitesquare = None

        # 대결 상대 체혁바
        self.img_info_hpbar_bg    = None
        self.img_info_hpbar_hp    = None
        self.img_info_hpbar_frame = None
        self.e_nowhp = 0 # 대결 상대 현재 체력
        self.e_maxhp = 0 # 대결 상대 최대 체력

        # 플레이어 하트
        self.img_info_playerlife      = None
        self.img_info_playerlife_lost = None
        self.p_nowlife = 0 # 현재 플레이어 하트
        self.p_maxlife = 0 # 최대 플레이어 하트

        # 시간 정보
        self.nowtime = 0 # 시간 표시

        # 점수 정보
        self.score_nowstage = 0 # 현재 스테이지 점수
        self.score_all      = 0 # 전체 점수

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
        game_objects.font.draw(10, 600 - (10 + FONTSIZE // 2), f'(게임 플레이 시간 : {self.nowtime:.1f})', (0, 0, 0))

        # 스코어 표시
        game_objects.font.draw(10, 570 - (10 + FONTSIZE // 2), f'전체 점수 : {self.score_nowstage}', (0, 0, 0))
        game_objects.font.draw(10, 540 - (10 + FONTSIZE // 2), f'현재 스테이지 점수 : {self.score_all}', (0, 0, 0))
