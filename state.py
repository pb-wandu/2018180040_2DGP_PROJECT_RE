# -----------<상태들>-----------

# 이벤트 확인 함수 및 상태를 기록한 파일

from pico2d import * # pico2d 모듈
import objects # 상태 머신 및 오브젝트 모듈 import

# ----- 게임 흐름 -----

# (첫 시작, 또는 새로운 스테이지 진입)
# Ready        : 준비 상태

# (3개 단계를 반복)
# Standoff     : 대치 상태
# Action       : 동작
# ActionResult : 동작 결과

# (적의 HP가 0 이하가 되면)
# Finish       : 대결 완료

# ----- 이벤트 확인 함수 및 상태별 동작 -----

### 임시 함수
def temp(e):
    return False

# 스페이스 바 눌림
def space_down(e):
    return e[0] == "INPUT" and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

# 박자표 시간 업데이트
def timeupdate(obj):
    # nowtime 1틱씩 진행
    obj.nowtick += 1
    # maxtime 초과시 0틱으로 초기화
    if obj.nowtick > obj.maxtick:
        obj.nowtick = 0

    ### 테스트용 - 박자 표시
    if obj.nowtick % 100 == 0 and obj.nowtick != 0:
        ### 테스트용 - 큰박자
        if obj.nowtick == obj.maxtick:
            print("<큰 박자> 박자표 [4 / 4] 박자")
        ### 테스트용 - 그 외
        else:
            print(f"박자표 [{int(obj.nowtick / 100)} / 4] 박자")

    # nowtime 1틱만큼의 지연 시간
    delay(obj.tick1time)

# ----- 각 world 상태별 상세 -----

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
        pass

"""
# Action (동작)
class Action:
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