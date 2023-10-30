# ----------<게임 프레임워크>----------

# 모드 2 - 게임 메뉴
# (상태 머신 클래스와 각 상태 포함)

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

# ----- 모듈 import -----

from pico2d import *    # pico2d 모듈 import
import objects          # 상태 머신 및 오브젝트 모듈 import
from functions import * # 이벤트 및 오브젝트별 동작 모듈 import

import gamemode_2_gamemenu # 게임 모드 gamemenu 모듈 import

import game_world
import game_framework

import gamemode_1_mainmenu # 게임 모드 mainmenu 모듈 import

# ----- 게임 프레임워크 동작 함수들 -----

def handle_events():

    events = get_events()
    delay(0.01)

    for event in events:
        # SDL_QUIT일 경우 게임 종료
        if event.type == SDL_QUIT:
            game_framework.quit()

        # esc키 누를 경우 메인메뉴로 이동
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(gamemode_1_mainmenu)

        # 그 외
        else:
            # 플레이어 동작에 따른 이벤트 수행
            objects.player.handle_event(event)

def init():
    # 월드 초기 설정
    game_world.init_world()

    ### 테스트용
    print("### gamemenu 진입")
    print("### objects에 있는 오브젝트들")
    for layer in game_world.objects:
        for obj in layer:
            print(obj)

def finish():
    # 월드 있는 모든 오브젝트 지우기
    game_world.clear_objects()

    print("### gamemenu에서 나가기")
    pass

def update():
    # 월드 업데이트
    game_world.update_allobject()

def draw():
    clear_canvas()
    # 월드에 있는 모든 오브젝트 렌더링
    game_world.render_allobject()
    update_canvas()

def pause():
    # boy.wait_time = 10000000000000000000000
    pass

def resume():
    # boy.wait_time = get_time()
    pass

# ----- gamemenu 각 상태별 동작 상세 클래스 -----

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
            timeupdate(obj, "Standoff") # 박자표 시간 업데이트
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
            timeupdate(obj, "Action") # 박자표 시간 업데이트
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

# ----- 상태 머신 클래스 -----

class StateMachine:

    # 초기 상태 설정
    def __init__(self):
        self.cur_state = Ready # 초기 상태 : Ready 상태
        self.now_action = None # 초기 상태 : 현재 동작 없음

        # 동작 전환
        self.transitions = {
            Ready: {space_down: Standoff},
            Standoff: {punch_activated: Action},
            Action: {func_temp: Standoff}
        }

    # 상태 머신 시작
    def start(self):
        self.cur_state.enter()

    # 상태 머신 event 관리
    def handle_event(self, e):
        # event를 확인하고 현재 상태를 next_state로 지정한다
        for check_event, next_state in self.transitions[self.cur_state].items():
            # self.transitions{ }에 저장되어 있는대로
            if check_event(e):
                self.cur_state.exit()       # 현재 상태에서 exit
                self.cur_state = next_state # 새로운 state 지정
                self.cur_state.enter()      # 새로운 상태로 enter
                return True
        return False

    # update와 draw는 state_machine의 현재 상태에서
    # 그 오브젝트에 대한 동작을 수행한다
    # (참고 : 상태 머신 자체는 update하거나 draw할 내용 없음)

    def update(self):
        self.cur_state.do(StateMachine)

    def draw(self):
        self.cur_state.draw(StateMachine)

# 상태 머신 (world에 실물이 없는 가상 머신이다)
state_machine = StateMachine() # 상태 머신 오브젝트

