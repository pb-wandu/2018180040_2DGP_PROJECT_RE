# -----------<상태들>-----------

# 이벤트 확인 함수 및 상태를 기록한 파일

import statemachine_and_objects # 상태 머신 및 오브젝트 모듈 import

# Ready        : 준비 상태
# Standoff     : 대치 상태
# Action       : 동작
# ActionResult : 동작 결과
# Finish       : 대결 완료

# ----- 이벤트 확인 함수들 -----

# 키 입력시
def keyinput(e, info, type_in, key_in):
    return e[0] == info and e[1].type == type_in and e[1].key == key_in

# a키 눌림 - 이건 임시로 둔 것
def a_down(e):
    keyinput(e, "INPUT", SDL_KEYDOWN, SDLK_a)

# 임시 함수
def temp(e):
    return False

# ----- 각 상태별 상세 -----

# Ready (준비 상태)
class Ready:
    @staticmethod
    def enter(obj, e):
        pass

    @staticmethod
    def do(obj):
        pass

    @staticmethod
    def draw(obj):
        pass

    @staticmethod
    def exit(obj, e):
        print("Idle exit")
        pass

# Standoff (대치 상태)
class Standoff:
    @staticmethod
    def enter(obj, e):

        ### 상태 클래스를 호출한 오브젝트가 무엇인지 판단 (임시)
        if type(obj) == statemachine_and_objects.Player:
            print("대치 상태(Standoff) - enter by Player")
        # elif type(obj) == statemachine_and_objects.Enemy:
        #    print("대치 상태(Standoff) - enter by Enemy")

        pass

    @staticmethod
    def do(obj):
        pass

    @staticmethod
    def draw(obj):
        pass

    @staticmethod
    def exit(obj, e):
        pass

# Action (동작)
class Action:
    @staticmethod
    def enter(obj, e):
        pass

    @staticmethod
    def do(obj):
        pass

    @staticmethod
    def draw(obj):
        pass

    @staticmethod
    def exit(obj, e):
        pass

# ActionResult (동작 결과)
class ActionResult:
    @staticmethod
    def enter(obj, e):
        pass

    @staticmethod
    def do(obj):
        pass

    @staticmethod
    def draw(obj):
        pass

    @staticmethod
    def exit(obj, e):
        pass

# Finish (대결 완료)
class Finish:
    @staticmethod
    def enter(obj, e):
        pass

    @staticmethod
    def do(obj):
        pass

    @staticmethod
    def draw(obj):
        pass

    @staticmethod
    def exit(obj, e):
        pass

