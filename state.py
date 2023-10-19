# -----------<상태들>-----------

# 이벤트 확인 함수 및 상태를 기록한 파일

from pico2d import * # pico2d 모듈
import objects # 상태 머신 및 오브젝트 모듈 import
# import images # 이미지 저장 모듈 import

# ----- 게임 흐름 -----

# (첫 시작, 또는 새로운 스테이지 진입)
# Ready        : 준비 상태

# (3개 단계를 반복)
# Standoff     : 대치 상태
# Action       : 동작
# ActionResult : 동작 결과

# (적의 HP가 0 이하가 되면)
# Finish       : 대결 완료

# ----- 이벤트 확인 함수 -----

### 임시 함수
def temp(e):
    return False

# 스페이스 바 눌림
def space_down(e):
    return e[0] == "INPUT" and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

# ----- 각 오브젝트별 상세 동작 및 그리기 -----

# 플레이어 - 펀치 실행
def punch_activated(e):
    """
    if 키보드 왼쪽 5줄 중 하나를 눌렀다면:
        player.nowpunchhand = "left"
    elif 키보드 오른쪽 5줄 중 하나를 눌렀다면:
        player.nowpunchhand = "left"
    else: # 다른 키를 눌렀다면
        player.nowpunchhand = None
    """
    return False ### 임시

# 박자표 - 시간 업데이트
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

# 박자표 그리기
def draw_beattimer(obj):
    
    # 박자표 이미지
    img_beat_small = load_image('img_beat_small.png')
    img_beat_big = load_image('img_beat_big.png')

    beatnum = obj.beatnum # 박자 수

    ### 박자표 중심은 '400, 400' (임시)
    SIZEX, SIZEY     = 100, 100 # 이미지 크기
    CENTERX, CENTERY = 400, 500 # 박자표 중심

    # 박자표 이미지 list에서 - index는 list에서의 위치, beat는 실제 값
    for index, beat in enumerate(obj.beat_image_list):

        # 이미지 그리기 시작하는 위치
        startx = (CENTERX - (beatnum-1) * SIZEX / 2) + (index * SIZEX)
        starty = CENTERY

        # 해당 박자가 없으면 - 그리기 종료
        if beat == None:
            img = None
            break

        # 해당 박자가 작은 박자이면 - 작은 박자 이미지 그리기
        elif beat == "small":
            img_beat_small.draw(startx, starty, SIZEX, SIZEY)

        # 해당 박자가 큰 박자이면 - 큰 박자 이미지 그리기
        elif beat == "big":
            img_beat_big.draw(startx, starty, SIZEX, SIZEY)

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

        # 플레이어
        if obj == objects.player:
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

        # 펀치로 인한 상태 종료시
        if punch_activated(e):
            # 플레이어의 펀치 동작 수행
            player.punch_action()

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

        # 플레이어
        if obj == objects.player:
            pass

        # 박자표
        elif obj == objects.beattimer:
            draw_beattimer(obj) # 박자표 그리기
            pass

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