# ----------<'모드 2 - 게임 메뉴'용 함수들>----------

from pico2d import *    # pico2d 모듈 import
import objects          # 상태 머신 및 오브젝트 모듈 import

import gamemode_2_1_state as state # 상태 관련 모듈 import

# ----- 함수들 -----

# 글러브 - 펀치 동작에 따른 위치설정
def setglovespos():

    if objects.player.nowpunchhand == None:
        objects.glove_l.setpos(250, 80)
        objects.glove_r.setpos(550, 80)

    elif objects.player.nowpunchhand == "left":
        objects.glove_l.setpos(250+100, 80+120)
        objects.glove_r.setpos(550, 80)

    elif objects.player.nowpunchhand == "right":
        objects.glove_l.setpos(250, 80)
        objects.glove_r.setpos(550-100, 80+120)

# 박자표 - 시간 업데이트 (1틱 간격)
def timeupdate(obj, nowstate):
    global timer_setglovepos

    # 왼손 또는 오른손 펀치를 날리고 있자면
    if objects.player.nowpunchhand == "left" or objects.player.nowpunchhand == "right":
        timer_setglovepos += 1
        # 펀치를 날린지 일정 시간이 지나면 펀치중인 손을 없음으로 초기화
        if timer_setglovepos >= 30:
            objects.player.nowpunchhand = None
            timer_setglovepos = 0
            setglovespos() # 글러브 위치설정

    # nowtime 1틱씩 진행
    obj.nowtick += 1

    # 해당 오브젝트의 박자 수에서 1박자가 더 넘어가면 0틱으로 초기화
    nextbeattick = obj.maxtick * ((obj.beatnum + 1) / obj.beatnum)
    if obj.nowtick > nextbeattick:
        obj.nowtick = 0

    # 펀치중이라면
    if state.state_machine.now_action == "punch":

        # 펀치 쿨타임 감소
        if objects.beattimer.punch_cooltime > 0:
            objects.beattimer.punch_cooltime -= 1

            # 쿨타임이 0이 되었다면
            if objects.beattimer.punch_cooltime <= 0:
                # 현재 하는 동작 없음
                state.now_action = None

                ### 테스트용
                print(f"펀치 쿨타임 초기화 완료")
        else:
            pass

    ### 테스트용 - 박자 표시
    if obj.nowtick % obj.ticknum == 0 and obj.nowtick != 0:
        ### 큰 박자
        if obj.nowtick == obj.maxtick:
            print(f"<큰 박자> 박자표 [{obj.beatnum} / {obj.beatnum}] 박자")
            pass
        ### 그 외
        elif int(obj.nowtick / obj.ticknum) <= obj.beatnum:
            print(f"박자표 [{int(obj.nowtick / obj.ticknum)} / {obj.beatnum}] 박자")
            pass


# 배경 그리기
def draw_bg(obj):
    if obj.image == None:
        obj.image = load_image('img_background.png')

    obj.image.draw(400, 300, 800, 600)  # 배경 그리기

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
    img_punch_eff_crit      = load_image('img_punch_eff_crit.png')      # 명중시 효과
    img_punch_eff_crit_text = load_image('img_punch_eff_crit_text.png') # 명중시 텍스트
    img_punch_eff_hit       = load_image('img_punch_eff_hit.png')       # 맞힘시 효과
    img_punch_eff_hit_text  = load_image('img_punch_eff_hit_text.png')  # 맞힘시 텍스트
    img_punch_eff_miss      = load_image('img_punch_eff_miss.png')      # 빗나감시 효과
    img_punch_eff_miss_text = load_image('img_punch_eff_miss_text.png') # 빗나감시 텍스트

    # obj == objects.player
    # 펀치 성공 상황에 따른 이펙트 표시

    # 명중
    if obj.ifpunchsuccess == "crit":
        ### 추가 예정
        pass

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

# 박자표 그리기
def draw_beattimer(obj):
    img_beat_bg = load_image('img_beat_bg.png')  # 박자 배경
    img_beat_effect = load_image('img_beat_effect.png')  # 현재 박자 이펙트
    img_beat_small = load_image('img_beat_small.png')  # 작은 박자
    img_beat_big = load_image('img_beat_big.png')  # 큰 박자

    beatnum = obj.beatnum  # 박자 수

    SIZE_BG_X, SIZE_BG_Y = 100, 100  # 박자표 틀 이미지 크기
    SIZE_EF_X, SIZE_EF_Y = 90, 90  # 박자표 효과 이미지 크기
    SIZE_BEAT_BIG_X, SIZE_BEAT_BIG_Y = 70, 70  # 큰 박자 이미지 크기
    SIZE_BEAT_SMALL_X, SIZE_BEAT_SMALL_Y = 40, 40  # 작은 박자 이미지 크기

    CENTERX, CENTERY = 400, 500  # 박자표 중심

    # 박자표 이미지 list에서 - index는 list에서의 위치, beat는 실제 값
    for index, beatimg in enumerate(obj.beat_image_list):

        # 이미지 그리기 시작하는 위치
        startx = (CENTERX - (beatnum - 1) * SIZE_BG_X / 2) + (index * SIZE_BG_X)
        starty = CENTERY

        # 해당 박자가 없으면 - 그리기 종료
        if beatimg == None:
            break

        else:

            # 박자 배경 그리기
            img_beat_bg.draw(startx, starty, SIZE_BG_X, SIZE_BG_Y)

            # 박자 이펙트 그리기
            if index == (obj.nowtick // obj.ticknum - 1):
                img_beat_effect.draw(startx, starty, SIZE_EF_X, SIZE_EF_Y)

            # 해당 박자가 작은 박자이면 -
            if beatimg == "small":

                # 작은 박자 이미지 그리기
                img_beat_small.draw(startx, starty, SIZE_BEAT_SMALL_X, SIZE_BEAT_SMALL_Y)

            # 해당 박자가 큰 박자이면 - 큰 박자 이미지 그리기
            elif beatimg == "big":

                # 큰 박자 이미지 그리기
                img_beat_big.draw(startx, starty, SIZE_BEAT_BIG_X, SIZE_BEAT_BIG_Y)