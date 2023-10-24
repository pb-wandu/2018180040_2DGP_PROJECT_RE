# -----------<상태들>-----------

# world 상태를 기록한 파일

from pico2d import *    # pico2d 모듈 import
import objects          # 상태 머신 및 오브젝트 모듈 import
from functions import * # 이벤트 및 오브젝트별 동작 모듈 import

# ----- 게임 흐름 -----

### (예정) Main (게임 메인 화면) 만들기

# (첫 시작, 또는 새로운 스테이지 진입)
# Ready        : 준비 상태

# (3개 단계를 반복)
# Standoff     : 대치 상태
# Action       : 동작
# ActionResult : 동작 결과

# (적의 HP가 0 이하가 되면)
# Finish       : 대결 완료

# ----- world 각 상태별 동작 상세 -----

# Ready (준비 상태)
class Ready:

    # 상태 진입
    @staticmethod
    def enter():
        print("Ready (준비 상태) enter")
        pass

    # 상태 종료
    @staticmethod
    def exit():
        print("Ready (준비 상태) exit")
        pass

    # 현 상태에서 각 오브젝트에 따른 동작
    @staticmethod
    def do(obj):

        # 플레이어
        if obj == objects.player:
            pass

        # 박자표
        elif obj == objects.beattimer:
            # Ready 상태에서는 박자표 시간 업데이트를 수행하지 않음
            pass

        pass

    # 현 상태에서 각 오브젝트 그리기
    @staticmethod
    def draw(obj):

        # 상태에 따른 정보 표시
        draw_state_info("Ready")

        # 배경
        if obj == objects.background:
            draw_bg(obj)  # 배경 그리기
            pass

        # 플레이어
        elif obj == objects.player:
            pass

        # 글러브
        elif obj == objects.glove_l or obj == objects.glove_r:
            draw_glove(obj) # 글러브 그리기
            pass

        # 박자표
        elif obj == objects.beattimer:
            # Ready 상태에서는 박자표를 그리지 않음
            pass

        pass

# Standoff (대치 상태)
class Standoff:
    # 상태 진입
    @staticmethod
    def enter():
        print("Standoff (대치 상태) enter")
        pass

    # 상태 종료
    @staticmethod
    def exit():

        print("Standoff (대치 상태) exit")
        pass

    # 현 상태에서 각 오브젝트에 따른 동작
    @staticmethod
    def do(obj):

        # 플레이어
        if obj == objects.player:
            pass

        # 박자표
        elif obj == objects.beattimer:
            # 박자표 시간 업데이트
            timeupdate(obj)
            pass

        pass

    # 현 상태에서 각 오브젝트 그리기
    @staticmethod
    def draw(obj):

        # 상태에 따른 정보 표시
        draw_state_info("Standoff")

        # 배경
        if obj == objects.background:
            draw_bg(obj) # 배경 그리기
            pass

        # 플레이어
        elif obj == objects.player:
            pass

        # 글러브
        elif obj == objects.glove_l or obj == objects.glove_r:
            draw_glove(obj) # 글러브 그리기
            pass

        # 박자표
        elif obj == objects.beattimer:
            draw_beattimer(obj) # 박자표 그리기
            pass

        pass

# Action (동작)
class Action:
    @staticmethod
    def enter():
        print("Action (동작 상태) enter")
        pass

    # 상태 종료
    @staticmethod
    def exit():

        print("Action (동작 상태) exit")
        pass

    # 현 상태에서 각 오브젝트에 따른 동작
    @staticmethod
    def do(obj):

        # 상태에 따른 정보 표시
        draw_state_info("Action")

        # 플레이어
        if obj == objects.player:
            pass

        # 박자표
        elif obj == objects.beattimer:
            pass

        pass

    # 현 상태에서 각 오브젝트 그리기
    @staticmethod
    def draw(obj):

        # 배경
        if obj == objects.background:
            draw_bg(obj) # 배경 그리기
            pass

        # 플레이어
        elif obj == objects.player:
            pass

        # 글러브
        elif obj == objects.glove_l or obj == objects.glove_r:
            draw_glove(obj) # 글러브 그리기
            pass

        # 박자표
        elif obj == objects.beattimer:
            draw_beattimer(obj) # 박자표 그리기
            pass

        pass

"""
# ActionResult (동작 결과)
class ActionResult:
    @staticmethod
    def enter():
        pass

    @staticmethod
    def exit():
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass

# Finish (대결 완료)
class Finish:
    @staticmethod
    def enter():
        pass

    @staticmethod
    def exit():
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass
"""