# ----------<'모드 2 - 게임 메뉴'용 게임 정보>----------

# 게임 정보들을 기록한 파일

from pico2d import *    # pico2d 모듈 import

import game_time    # 시간 관련 모듈 import
import game_objects # 오브젝트 모듈 import

import gamemode_2_1_state       as gamestate # 상태 관련 모듈 import
import gamemode_2_1_gameinfo    as gameinfo  # 게임 정보 모음 모듈 import
import game_playerAndEnemy      as PAE       # 플레이어 및 대결 상대 모듈 import

# 게임 정보 상수들

# (공격) 명중 / 맞힘 / 빗나감 : 각각 20 / 10 / 0 HP 감소 (적)
POINT_ATKCRIT, POINT_ATKHIT, POINT_ATKMISS = 20, 10, 0
# (방어) 회피 / 스침 / 맞음  : 각각 0 / 1 / 2 하트 감소 (플레이어)
POINT_DEFSUCCESS, POINT_DEFHALF, POINT_DEFMISS = 0, 1, 2

SCORE_HIT   = 100 # 맞힘 성공시 기본 점수
SCORE_CRIT  = 250 # 명중 성공시 점수
SCORE_COMBO = 10  # 콤보당 추가 점수

# ----- 게임 정보 클래스 -----

class Gameinfomation:

    def __init__(self):

        self.img_whitesquare = None

        # 대결 상대 체력바
        self.img_info_hpbar_bg    = None
        self.img_info_hpbar_hp    = None
        self.img_info_hpbar_frame = None
        self.e_nowhp = 0 # 대결 상대 현재 체력
        self.e_maxhp = 0 # 대결 상대 최대 체력

        # 플레이어 하트
        self.img_info_playerlife      = None
        self.img_info_playerlife_half = None
        self.img_info_playerlife_lost = None
        self.p_nowlife = 0 # 현재 플레이어 하트
        self.p_maxlife = 0 # 최대 플레이어 하트

        # 시간 정보
        self.nowtime = 0 # 시간 표시

        # 점수 정보
        self.score_nowstage = 0 # 현재 스테이지 점수
        self.score_all      = 0 # 전체 점수

        # 콤보 정보 (연속으로 맞힌 수)
        self.img_combo = None # 콤보 표시용 이미지
        self.nowcombo = 0     # 현재 콤보

        # ----- 스테이지 정보 -----

        # 첫 대결 상대 지정
        self.nowStage = 1 # 현재 스테이지
        self.nowWave  = 1 # 현재 웨이브


    def update(self):
        # 게임 시간 업데이트
        self.nowtime = get_time() - game_time.gametimer.start_time
        pass

    def draw(self):

        ### 상태 머신이 Ready상태가 아닐 경우 (임시)
        if gamestate.state_machine.cur_state != gamestate.Ready:
            # 하트 및 체력바 그리기
            PAE.draw_life_hp_info(self,
                self.p_nowlife, self.p_maxlife, self.e_nowhp, self.e_maxhp)

            # 체력바 옆에 현재 체력/전체 체력 표시
            FONTSIZE = 20
            game_objects.font.draw(420, 480 - (10 + FONTSIZE // 2),
                                f'{self.e_nowhp} / {self.e_maxhp}', (0, 0, 0))

        # 폰트 크기
        FONTSIZE = 20

        # 게임 시간 및 현재 진행 스테이지 표시
        game_objects.font.draw(20, 590 - (10 + FONTSIZE // 2), f'(게임 플레이 시간 : {self.nowtime:.1f})', (0, 0, 0))
        game_objects.font.draw(20, 560 - (10 + FONTSIZE // 2), f'전체 점수 : {self.score_all}', (0, 0, 0))
        game_objects.font.draw(20, 530 - (10 + FONTSIZE // 2), f'현재 스테이지 점수 : {self.score_nowstage}', (0, 0, 0))

        # 스테이지 현황 표시
        game_objects.font.draw(20, 500 - (10 + FONTSIZE // 2), f'--<{self.nowStage}스테이지 - {self.nowWave}wave>--', (0, 0, 0))

        # 콤보 표시 (1콤보 이상일 때)
        if self.nowcombo >= 1:
            # 이미지 초기 지정
            if self.img_combo == None:
                self.img_combo = load_image('./resource_image/img_info_combo.png')

            # 콤보 이미지 그리고 몇 콤보인지 표시
            self.img_combo.draw(680, 500, 200, 120)
            game_objects.font.draw(645, 500, f'<{self.nowcombo}콤보> !!', (0, 0, 0))

# 게임 정보
gameinfomation = Gameinfomation()
            
# ----- 게임 정보 표시 함수 -----

# 박자표 그리기
def draw_beattimer(obj):
    if obj.img_beat_bg == None:
        obj.img_beat_bg = load_image('./resource_image/img_beat_bg.png')  # 박자 배경
    if obj.img_beat_effect == None:
        obj.img_beat_effect = load_image('./resource_image/img_beat_effect.png')  # 현재 박자 이펙트
    if obj.img_beat_small == None:
        obj.img_beat_small = load_image('./resource_image/img_beat_small.png')  # 작은 박자
    if obj.img_beat_big == None:
        obj.img_beat_big = load_image('./resource_image/img_beat_big.png')  # 큰 박자

    beatnum = obj.beatnum  # 박자 수

    SIZE_BG_X, SIZE_BG_Y = 100, 100  # 박자표 틀 이미지 크기
    SIZE_EF_X, SIZE_EF_Y = 90, 90  # 박자표 효과 이미지 크기
    SIZE_BEAT_BIG_X, SIZE_BEAT_BIG_Y = 70, 70  # 큰 박자 이미지 크기
    SIZE_BEAT_SMALL_X, SIZE_BEAT_SMALL_Y = 40, 40  # 작은 박자 이미지 크기

    CENTERX, CENTERY = 400, 540  # 박자표 중심

    # 박자표 이미지 list에서 - index는 list에서의 위치, beat는 실제 값
    for index, beatimg in enumerate(obj.beat_image_list):

        # 이미지 그리기 시작하는 위치
        startx = (CENTERX - (beatnum - 1) * SIZE_BG_X / 2) + (index * SIZE_BG_X)
        starty = CENTERY

        # 해당 박자가 없으면 - 그리기 종료
        if beatimg == None:
            break

        else:

            # 박자 배경 그리기
            obj.img_beat_bg.draw(startx, starty, SIZE_BG_X, SIZE_BG_Y)

            # 박자 이펙트 그리기
            if index == (obj.nowtick // obj.ticknum - 1):
                obj.img_beat_effect.draw(startx, starty, SIZE_EF_X, SIZE_EF_Y)

            # 해당 박자가 작은 박자이면 -
            if beatimg == "small":
                # 작은 박자 이미지 그리기
                obj.img_beat_small.draw(startx, starty, SIZE_BEAT_SMALL_X, SIZE_BEAT_SMALL_Y)

            # 해당 박자가 큰 박자이면 - 큰 박자 이미지 그리기
            elif beatimg == "big":
                # 큰 박자 이미지 그리기
                obj.img_beat_big.draw(startx, starty, SIZE_BEAT_BIG_X, SIZE_BEAT_BIG_Y)
    pass