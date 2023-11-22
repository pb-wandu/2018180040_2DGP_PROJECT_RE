# ----------<플레이어, 대결 상대>----------

# 플레이어, 대결 상대를 기록한 파일

from pico2d import *  # pico2d 모듈 import

# '모드 2 - 게임 메뉴'용 상태 머신 import
import gamemode_2_1_state as gamestate # 상태 관련 모듈 import

# 그 외 import
import game_world                       # 게임 월드 모듈 import
from game_objects import *              # 게임 오브젝트 모듈 import
import game_PAE_ePatternAndWave as EPAW # 대결 상대 패턴 import

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
    image = None  # 이미지
    glovedir = None  # 글러브 방향
    x, y = 0, 0  # 글러브 위치

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
        pass

    @staticmethod
    def draw():
        pass

    # 바운딩 박스 가져오기
    def get_bb(self):
        return self.x - 90, self.y - 90, self.x + 90, self.y + 90

# ----- 대결 상대 클래스 -----

class Enemy:

    def __init__(self, beatnum, pattern):
        self.x, self.y = 400, 300  # 대결 상대 x, y 위치

        # 대결 상대 동작 패턴 지정
        self.nowPattern = 0
        self.maxPattern = beatnum
        self.pattern    = pattern

    # 대결 상대 동작 패턴 지정
    def setPattern(self, beatnum, pattern):
        self.maxPattern = beatnum
        self.pattern    = pattern

    # 대결 상대 다음 동작 패턴
    def nextPattern(self):
        if self.nowPattern < self.maxPattern:
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

# ----- 클래스별 실제 오브젝트 -----

# 플레이어 오브젝트
player = Player()

# 대결 상대 오브젝트 생성시에 첫 패턴(1-1)을 지정
enemy = Enemy(EPAW.nowPatternNum-1, EPAW.nowEnemyPattern)
