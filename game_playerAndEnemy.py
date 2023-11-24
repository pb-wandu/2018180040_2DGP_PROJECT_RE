# ----------<플레이어, 대결 상대>----------

# 플레이어, 대결 상대를 기록한 파일

from pico2d import *  # pico2d 모듈 import

# '모드 2 - 게임 메뉴'용 상태 머신 import
import gamemode_2_1_state    as gamestate # 상태 관련 모듈 import
import gamemode_2_1_gameinfo as gameinfo  # 게임 정보 모듈 import

# 그 외 import

import game_background # 게임 배경 모듈 import
import game_world      # 게임 월드 모듈 import

from game_objects import *              # 게임 오브젝트 모듈 import
import game_PAE_ePatternAndWave as EPAW # 대결 상대 패턴 import


# 적 체력, 플레이어 하트
enemyhp = 50
playerlife = 3

# ----- 플레이어 관련 함수 -----

# 글러브 - 펀치 동작에 따른 위치설정
def setglovespos():

    if player.nowpunchhand == None:
        player.glove_l.setpos(250, 80)
        player.glove_r.setpos(550, 80)

    elif player.nowpunchhand == "left":
        player.glove_l.setpos(250+100, 80+120)
        player.glove_r.setpos(550, 80)

    elif player.nowpunchhand == "right":
        player.glove_l.setpos(250, 80)
        player.glove_r.setpos(550-100, 80+120)


# 글러브 그리기
def draw_glove(obj):
    if obj.image == None:
        # 글러브 방향에 따라 이미지 표시하기
        if obj.glovedir == "left":
            obj.image = load_image('img_glove_left.png')  # 왼쪽 글러브
        elif obj.glovedir == "right":
            obj.image = load_image('img_glove_right.png')  # 오른쪽 글러브

    # 글러브 정보
    x, y = obj.x, obj.y  # x, y 위치
    SIZEX, SIZEY = 240, 240  # x, y 크기

    # 글러브 그리기
    obj.image.draw(x, y, SIZEX, SIZEY)

# 펀치 이펙트 그리기
def draw_puncheffect(obj):
    img_punch_eff_crit = load_image('img_punch_eff_crit.png')  # 명중시 효과
    img_punch_eff_crit_text = load_image('img_punch_eff_crit_text.png')  # 명중시 텍스트
    img_punch_eff_hit = load_image('img_punch_eff_hit.png')  # 맞힘시 효과
    img_punch_eff_hit_text = load_image('img_punch_eff_hit_text.png')  # 맞힘시 텍스트
    img_punch_eff_miss = load_image('img_punch_eff_miss.png')  # 빗나감시 효과
    img_punch_eff_miss_text = load_image('img_punch_eff_miss_text.png')  # 빗나감시 텍스트

    # obj == pne.player
    # 펀치 성공 상황에 따른 이펙트 표시

    # 명중
    if obj.ifpunchsuccess == "crit":

        if obj.nowpunchhand == "left":
            img_punch_eff_crit.draw(360, 260, 280, 280)
            img_punch_eff_crit_text.draw(450, 360, 80, 40)
        elif obj.nowpunchhand == "right":
            img_punch_eff_crit.draw(440, 260, 280, 280)
            img_punch_eff_crit_text.draw(290, 360, 80, 40)

    # 맞힘
    elif obj.ifpunchsuccess == "hit":

        if obj.nowpunchhand == "left":
            img_punch_eff_hit.draw(360, 260, 280, 280)
            img_punch_eff_hit_text.draw(450, 360, 60, 40)
        elif obj.nowpunchhand == "right":
            img_punch_eff_hit.draw(440, 260, 280, 280)
            img_punch_eff_hit_text.draw(360, 360, 60, 40)

    # 빗나감
    elif obj.ifpunchsuccess == "failed":

        if obj.nowpunchhand == "left":
            img_punch_eff_miss.draw(370, 260, 220, 220)
            img_punch_eff_miss_text.draw(450, 360, 80, 40)
        elif obj.nowpunchhand == "right":
            img_punch_eff_miss.draw(430, 260, 220, 220)
            img_punch_eff_miss_text.draw(380, 360, 80, 40)

# ----- 플레이어 클래스 -----

class Player:

    def __init__(self):
        self.nowpunchhand = None  # 현재 주먹을 지른 손
        self.ifpunchsuccess = None  # 펀치 성공 여부
        self.x, self.y = 400, 100  # 플레이어 x, y 위치
        self.glove_l = Player_Glove("left", 250, 80)
        self.glove_r = Player_Glove("right", 550, 80)

        self.timer_punch = 0 # 펀치 동작중 타이머

        pass

    @staticmethod
    def handle_event(event):
        # 입력받은 값에 따라 state_machine에서 event를 수행한다
        # e[0] = 이벤트 종류, e[1] = 실제 이벤트 값
        gamestate.state_machine.handle_event(('INPUT', event))

    # update와 draw는 state_machine의 현재 상태에서
    # 그 클래스에 대한 실제 오브젝트의 동작을 수행한다

    @staticmethod
    def update():
        gamestate.state_machine.cur_state.do(player)

        # 글러브 업데이트
        gamestate.state_machine.cur_state.do(player.glove_l)
        gamestate.state_machine.cur_state.do(player.glove_r)
        pass

    @staticmethod
    def draw():
        gamestate.state_machine.cur_state.draw(player)
        gamestate.state_machine.cur_state.draw(player.glove_l)
        gamestate.state_machine.cur_state.draw(player.glove_r)

        ### 테스트용 - 바운딩 박스 그리기
        draw_rectangle(*player.get_bb())
        draw_rectangle(*player.glove_l.get_bb())
        draw_rectangle(*player.glove_r.get_bb())
        pass

    # 충돌 판정
    def handle_collision(self, group, other):
        """
        if group == 'glove-enemy':
            if 플레이어가 공격시 '명중' 또는 '맞힘'일 경우:
                동작
        if group == 'player-enemy':
            if 플레이어가 방어시 '맞음' 상태일 경우
                동작
        """
        pass

    # 바운딩 박스 가져오기
    def get_bb(self):
        return self.x - 240, self.y - 180, self.x + 240, self.y + 80

# ----- 플레이어 글러브 클래스 -----

class Player_Glove:
    image = None    # 이미지
    glovedir = None # 글러브 방향
    x, y = 0, 0     # 글러브 위치

    def __init__(self, dir, posx, posy):
        # 입력값에 따른 방향 지정
        self.glovedir = dir

        # 입력값에 따른 위치 지정
        self.x = posx
        self.y = posy

    # 글러브 위치 (재)지정
    def setpos(self, posx, posy):

        # 입력값에 따른 위치 지정
        self.x = posx
        self.y = posy

    @staticmethod
    def update():
        pass

    @staticmethod
    def draw():
        pass

    # 바운딩 박스 가져오기
    def get_bb(self):
        return self.x - 90, self.y - 90, self.x + 90, self.y + 90

# ----- 대결 상대 관련 함수 -----

# 펀치 동작에 따른 적 위치설정
def setenemyspos():

    if player.nowpunchhand == None:
        enemy.setpos(0, 0)

    elif player.nowpunchhand == "left":
        enemy.setpos(game_background.BGPUNCHMOVE, 0)

    elif player.nowpunchhand == "right":
        enemy.setpos(-game_background.BGPUNCHMOVE, 0)

# ----- 대결 상대 클래스 -----

class Enemy:

    def __init__(self, stage, wave):
        # 대결 상대 x, y 위치
        self.x, self.y = 400, 300

        # 대결 상대 동작 패턴 지정

        self.nowPattern = 0 # 현재 패턴 위치

        self.maxBeat     = EPAW.beatNum[stage - 1][wave - 1]           # 박자 개수
        self.patternNum  = EPAW.patternNum[stage - 1][wave - 1]        # 패턴 개수
        self.patternlist = EPAW.totalEnemyPattern[stage - 1][wave - 1] # 현재 패턴 전체

        pass

    # 대결 상대 위치 (재)지정
    def setpos(self, movedirx, movediry):
        # 입력값에 따른 위치 지정
        self.x = 400 + movedirx
        self.y = 300 + movediry

    # 대결 상대 동작 패턴 지정
    def setPattern(self, stage, wave):

        # 대결 상대 동작 패턴 지정

        self.nowPattern = 0 # 현재 패턴 위치

        self.maxBeat     = EPAW.beatNum[stage - 1][wave - 1]           # 박자 개수
        self.patternNum  = EPAW.patternNum[stage - 1][wave - 1]        # 패턴 개수
        self.patternlist = EPAW.totalEnemyPattern[stage - 1][wave - 1] # 현재 패턴 전체

    # 대결 상대 다음 동작 패턴
    def nextPattern(self):
        if self.nowPattern < self.patternNum-1:
            self.nowPattern += 1
        else:
            self.nowPattern = 0

    def handle_event(self, event):
        # 처리받을 입력이 없음
        pass

    # update와 draw는 state_machine의 현재 상태에서
    # 그 클래스에 대한 실제 오브젝트의 동작을 수행한다

    @staticmethod
    def update():
        gamestate.state_machine.cur_state.do(enemy)
        pass

    @staticmethod
    def draw():
        gamestate.state_machine.cur_state.draw(enemy)

        ### 테스트용 - 바운딩 박스 그리기
        draw_rectangle(*enemy.get_bb())
        pass

    # 충돌 판정
    def handle_collision(self, group, other):
        """
        if group == 'glove-enemy':
            if 플레이어가 공격시 '명중' 또는 '맞힘'일 경우:
                동작
        if group == 'player-enemy':
            if 플레이어가 방어시 '맞음' 상태일 경우
                동작
        """
        pass

    # 바운딩 박스 가져오기
    def get_bb(self):
        return self.x - 150, self.y - 100, self.x + 150, self.y + 120

# ----- 하트 및 체력바 그리기 함수 -----
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
    HPBARPOSX, HPBARPOSY = 330, 460 # 체력바 x, y위치
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

# ----- 클래스별 실제 오브젝트 -----

# 플레이어 오브젝트
player = Player()

# 대결 상대 오브젝트 생성시에 첫 패턴(1-1)을 지정
enemy = Enemy(1, 1)
