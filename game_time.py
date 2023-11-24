# ----------<시간 관련 코드>----------

# 시간 관련 클래스 및 함수를 기록한 파일

from pico2d import *  # pico2d 모듈 import

import game_objects               # 오브젝트 모듈 import
import game_playerAndEnemy as PAE # 플레이어 및 대결 상대 모듈 import

import gamemode_2_1_state    as gamestate # 상태 관련 모듈 import
import gamemode_2_1_gameinfo as gameinfo  # 게임 정보 관련 모듈 import

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

# 박자표 - 시간 업데이트 (1틱 간격)
def timeupdate(obj, nowstate):

    # 왼손 또는 오른손 펀치를 날리고 있자면
    if (PAE.player.nowpunchhand == "left"
            or PAE.player.nowpunchhand == "right"):
        PAE.player.timer_punch += 1
        # 펀치를 날린지 일정 시간이 지나면 펀치중인 손과 펀치 타이머를 초기화
        if PAE.player.timer_punch >= 30:
            PAE.player.nowpunchhand = None
            PAE.player.timer_punch = 0
            PAE.setglovespos() # 글러브 위치 설정

    # nowtime 1틱씩 진행
    obj.nowtick += 1

    # 해당 오브젝트의 박자 수에서 1박자가 더 넘어가면 0틱으로 초기화
    nextbeattick = obj.maxtick * ((obj.beatnum + 1) / obj.beatnum)
    if obj.nowtick > nextbeattick:
        obj.nowtick = 0

        # 대결 상대의 다음 동작 패턴 수행
        PAE.enemy.nextPattern()

        # 박자표의 박자 목록을 상대의 현재 동작으로 지정
        game_objects.beattimer.beat_image_list = PAE.enemy.patternlist[PAE.enemy.nowPattern]

    # 펀치중이라면
    if gamestate.state_machine.now_action == "punch":

        # 펀치 쿨타임 감소
        if game_objects.beattimer.punch_cooltime > 0:
            game_objects.beattimer.punch_cooltime -= 1

            # 쿨타임이 0이 되었다면
            if game_objects.beattimer.punch_cooltime <= 0:
                # 현재 하는 동작 없음
                gamestate.state_machine.now_action = None

                ### 테스트용
                print(f"펀치 쿨타임 초기화 완료")
        else:
            pass

    ### 테스트용 - 박자 표시
    if obj.nowtick % obj.ticknum == 0 and obj.nowtick != 0:

        nowbeat = int(obj.nowtick / obj.ticknum) # 현재 박자
        nowbeatimg = game_objects.beattimer.beat_image_list[nowbeat-1] # 현재 박자 이미지

        print(nowbeat, nowbeatimg)

        # 큰 박자인 경우
        if nowbeatimg == "big":
            print(f"<큰 박자> 박자표 [{obj.beatnum} / {obj.beatnum}] 박자")
            pass
        # 작은 박자인 경우
        elif nowbeatimg == "small":
            print(f"박자표 [{nowbeat} / {obj.beatnum}] 박자")
            pass


