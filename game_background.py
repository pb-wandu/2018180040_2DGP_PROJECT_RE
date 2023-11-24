# ----------<게임 배경>----------

# 게임 배경 관련 내용을 기록한 파일

from pico2d import *  # pico2d 모듈 import

import gamemode_2_1_state as gamestate # 상태 관련 모듈 import

import game_playerAndEnemy as PAE # 플레이어 및 대결 상대 모듈 import

# ----- 배경 클래스 -----

class Background:
    def __init__(self):
        self.image = load_image('img_background.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        # self.w = self.image.w
        # self.h = self.image.h

        self.window_left = 0
        self.window_bottom = 0

    # 펀치중인 손에 따라 배경 위치 바꾸기
    def update(self):

        if PAE.player.nowpunchhand == None:
            self.window_left = 0
            self.window_bottom = 0

        elif PAE.player.nowpunchhand == "left":
            self.window_left = -80
            self.window_bottom = 0

        elif PAE.player.nowpunchhand == "right":
            self.window_left = 80
            self.window_bottom = 0

    def draw(self):
        # gamestate.state_machine.cur_state.draw(self)
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)
