# ----------<게임 배경>----------

# 게임 배경 관련 내용을 기록한 파일

from pico2d import *  # pico2d 모듈 import

import gamemode_2_1_state as gamestate # 상태 관련 모듈 import

# ----- 배경 클래스 -----

# main에서의 배경화면
class Background_main:
    image = None

    def update(self):
        pass

    def draw(self):
        gamestate.state_machine.cur_state.draw(self)

    pass

# 게임 화면에서의 배경화면
class Background_game:
    image = None

    def update(self):
        pass

    def draw(self):
        gamestate.state_machine.cur_state.draw(self)

# ----- 배경 그리기 함수 -----

def draw_bg(obj):

    # 게임메뉴 배경
    if obj.image == None:
        obj.image = load_image('img_background.png')

    obj.image.draw(400, 300, 800, 600)  # 배경 그리기

# ----- 클래스별 실제 오브젝트 -----

# 배경 오브젝트
background_main = Background_main() # 메인메뉴 배경
background_game = Background_game() # 게임메뉴 배경

