# ----------<게임 타이머>----------

from pico2d import *  # pico2d 모듈 import

# ----- 타이머 클래스 -----

class Gametimer:
    start_time = 0 # 시작 시간
    now_time   = 0 # 현재 시간

    def __init__(self):
        self.start_time, self.now_time = 0, 0

    def updateTime(self):
        # 현재 시간 갱신
        self.now_time = get_time()
        pass

    # 게임 시작 시간 지정
    def setStartTime(self):
        # 현재 시간을 게임 시작 시간으로 지정
        self.start_time = get_time()

# 게임 타이머 오브젝트
gametimer = Gametimer()



