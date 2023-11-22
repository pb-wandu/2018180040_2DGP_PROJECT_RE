# ----------<'모드 2 - 게임 메뉴'용 게임 정보>----------

# 게임 정보들을 기록한 파일

from pico2d import *    # pico2d 모듈 import

import game_time    # 시간 관련 모듈 import
import game_objects # 오브젝트 모듈 import

import gamemode_2_1_state    as gamestate # 상태 관련 모듈 import
import gamemode_2_1_gameinfo as gameinfo  # 게임 정보 모음 모듈 import
import game_PAE_ePatternAndWave as EPAW   # 대결 상대 패턴 import

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
            gameinfo.draw_life_hp_info(self,
                self.p_nowlife, self.p_maxlife, self.e_nowhp, self.e_maxhp)

            # 체력바 옆에 현재 체력/전체 체력 표시
            FONTSIZE = 20
            game_objects.font.draw(420, 470 - (10 + FONTSIZE // 2),
                                f'{self.e_nowhp} / {self.e_maxhp}', (0, 0, 0))

        # 게임 시간 표시
        FONTSIZE = 16
        game_objects.font.draw(10, 600 - (10 + FONTSIZE // 2), f'(게임 플레이 시간 : {self.nowtime:.1f})', (0, 0, 0))

        # 현재 진행 스테이지 표시
        game_objects.font.draw(10, 570 - (10 + FONTSIZE // 2), f'전체 점수 : {self.score_all}', (0, 0, 0))
        game_objects.font.draw(10, 540 - (10 + FONTSIZE // 2), f'현재 스테이지 점수 : {self.score_nowstage}', (0, 0, 0))

        # 스테이지 현황 표시
        game_objects.font.draw(10, 470 - (10 + FONTSIZE // 2), f'<{self.nowStage}스테이지 - {self.nowWave}wave 진행중>', (0, 0, 0))

        # 콤보 표시 (1콤보 이상일 때)
        if self.nowcombo >= 1:
            # 이미지 초기 지정
            if self.img_combo == None:
                self.img_combo = load_image('img_info_combo.png')

            # 콤보 이미지 그리고 몇 콤보인지 표시
            self.img_combo.draw(680, 500, 200, 120)
            game_objects.font.draw(645, 500, f'<{self.nowcombo}콤보> !!', (0, 0, 0))

# 게임 정보
gameinfomation = Gameinfomation()
            
# ----- 게임 정보 표시 함수 -----

# 하트 및 체력바 그리기
def draw_life_hp_info(obj, p_nowlife, p_maxlife, e_nowhp, e_maxhp):
    if obj.img_info_hpbar_bg == None:
        obj.img_info_hpbar_bg = load_image('img_info_hpbar_bg.png')
    if obj.img_info_hpbar_hp == None:
        obj.img_info_hpbar_hp = load_image('img_info_hpbar_hp.png')
    if obj.img_info_hpbar_frame == None:
        obj.img_info_hpbar_frame = load_image('img_info_hpbar_frame.png')
    if obj.img_info_playerlife == None:
        obj.img_info_playerlife = load_image('img_info_playerlife.png')
    if obj.img_info_playerlife_lost == None:
        obj.img_info_playerlife_lost = load_image('img_info_playerlife_lost.png')

    if obj.img_whitesquare == None:
        obj.img_whitesquare = load_image('img_whitesquare.png')

    player_now_life, player_max_life = p_nowlife, p_maxlife # 플레이어 하트
    enemy_hp_left, enemy_hp_total = e_nowhp, e_maxhp # 적 체력

    HPBARLENGTH = 150 # 체력바 길이
    HPBARPOSX, HPBARPOSY = 330, 450 # 체력바 x, y위치
    hpnow_drawlength = HPBARLENGTH * (enemy_hp_left / enemy_hp_total) # 남은 체력 길이
    hpnowposx = HPBARPOSX - (HPBARLENGTH - hpnow_drawlength) / 2 # 남은 체력 현재 위치

    # 플레이어 하트 그리기
    for n in range(player_max_life):
        obj.img_whitesquare.draw(50, 50 + n * 50, 60, 60)
        obj.img_info_playerlife_lost.draw(50, 50 + n * 50, 30, 30)
    for n in range(player_now_life):
        obj.img_whitesquare.draw(50, 50 + n * 50, 60, 60)
        obj.img_info_playerlife.draw(50, 50 + n * 50, 30, 30)

    # 적 체력 그리기
    obj.img_info_hpbar_bg.draw   (HPBARPOSX, HPBARPOSY, HPBARLENGTH,      40)
    obj.img_info_hpbar_hp.draw   (hpnowposx, HPBARPOSY, hpnow_drawlength, 40)
    obj.img_info_hpbar_frame.draw(HPBARPOSX, HPBARPOSY, HPBARLENGTH,      40)

    pass

# 배경 그리기
def draw_bg(obj):

    # 게임메뉴 배경
    if obj.image == None:
        obj.image = load_image('img_background.png')

    obj.image.draw(400, 300, 800, 600)  # 배경 그리기

# 박자표 그리기
def draw_beattimer(obj):
    if obj.img_beat_bg == None:
        obj.img_beat_bg = load_image('img_beat_bg.png')  # 박자 배경
    if obj.img_beat_effect == None:
        obj.img_beat_effect = load_image('img_beat_effect.png')  # 현재 박자 이펙트
    if obj.img_beat_small == None:
        obj.img_beat_small = load_image('img_beat_small.png')  # 작은 박자
    if obj.img_beat_big == None:
        obj.img_beat_big = load_image('img_beat_big.png')  # 큰 박자

    beatnum = obj.beatnum  # 박자 수

    SIZE_BG_X, SIZE_BG_Y = 100, 100  # 박자표 틀 이미지 크기
    SIZE_EF_X, SIZE_EF_Y = 90, 90  # 박자표 효과 이미지 크기
    SIZE_BEAT_BIG_X, SIZE_BEAT_BIG_Y = 70, 70  # 큰 박자 이미지 크기
    SIZE_BEAT_SMALL_X, SIZE_BEAT_SMALL_Y = 40, 40  # 작은 박자 이미지 크기

    CENTERX, CENTERY = 400, 530  # 박자표 중심

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