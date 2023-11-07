# ----------<'모드 2 - 게임 메뉴'용 함수들>----------

from pico2d import * # pico2d 모듈 import

import game_objects        # 오브젝트 모듈 import
import game_playerAndEnemy # 플레이어 및 대결 상대 모듈 import

import gamemode_2_1_state as gamestate # 상태 관련 모듈 import

import game_timer # 타이머 모듈 import

# ----- 함수들 -----

# 글러브 - 펀치 동작에 따른 위치설정
def setglovespos():

    if game_playerAndEnemy.player.nowpunchhand == None:
        game_objects.glove_l.setpos(250, 80)
        game_objects.glove_r.setpos(550, 80)

    elif game_playerAndEnemy.player.nowpunchhand == "left":
        game_objects.glove_l.setpos(250+100, 80+120)
        game_objects.glove_r.setpos(550, 80)

    elif game_playerAndEnemy.player.nowpunchhand == "right":
        game_objects.glove_l.setpos(250, 80)
        game_objects.glove_r.setpos(550-100, 80+120)

# 박자표 - 시간 업데이트 (1틱 간격)
def timeupdate(obj, nowstate):
    global timer_setglovepos

    # 왼손 또는 오른손 펀치를 날리고 있자면
    if (game_playerAndEnemy.player.nowpunchhand == "left"
            or game_playerAndEnemy.player.nowpunchhand == "right"):
        timer_setglovepos += 1
        # 펀치를 날린지 일정 시간이 지나면 펀치중인 손을 없음으로 초기화
        if timer_setglovepos >= 30:
            game_playerAndEnemy.player.nowpunchhand = None
            timer_setglovepos = 0
            setglovespos() # 글러브 위치설정

    # nowtime 1틱씩 진행
    obj.nowtick += 1

    # 해당 오브젝트의 박자 수에서 1박자가 더 넘어가면 0틱으로 초기화
    nextbeattick = obj.maxtick * ((obj.beatnum + 1) / obj.beatnum)
    if obj.nowtick > nextbeattick:
        obj.nowtick = 0

    # 펀치중이라면
    if gamestate.state_machine.now_action == "punch":

        # 펀치 쿨타임 감소
        if game_objects.beattimer.punch_cooltime > 0:
            game_objects.beattimer.punch_cooltime -= 1

            # 쿨타임이 0이 되었다면
            if game_objects.beattimer.punch_cooltime <= 0:
                # 현재 하는 동작 없음
                gamestate.now_action = None

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

    # 게임메뉴 배경
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

    # obj == game_playerAndEnemy.player
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
    if obj.img_beat_bg == None:
        obj.img_beat_bg = load_image('img_beat_bg.png')  # 박자 배경
    if obj.img_beat_effect == None:
        obj.img_beat_effect = load_image('img_beat_effect.png')  # 현재 박자 이펙트
    if obj.img_beat_small == None:
        obj.img_beat_small = load_image('img_beat_small.png')  # 작은 박자
    if obj.img_beat_big == None:
        obj.img_beat_big = load_image('img_beat_big.png')  # 큰 박자

    beatnum = obj.beatnum  # 박자 수

    SIZE_BG_X, SIZE_BG_Y = 100, 100  # 박자표 틀 이미지 크기
    SIZE_EF_X, SIZE_EF_Y = 90, 90  # 박자표 효과 이미지 크기
    SIZE_BEAT_BIG_X, SIZE_BEAT_BIG_Y = 70, 70  # 큰 박자 이미지 크기
    SIZE_BEAT_SMALL_X, SIZE_BEAT_SMALL_Y = 40, 40  # 작은 박자 이미지 크기

    CENTERX, CENTERY = 400, 530  # 박자표 중심

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
            obj.img_beat_bg.draw(startx, starty, SIZE_BG_X, SIZE_BG_Y)

            # 박자 이펙트 그리기
            if index == (obj.nowtick // obj.ticknum - 1):
                obj.img_beat_effect.draw(startx, starty, SIZE_EF_X, SIZE_EF_Y)

            # 해당 박자가 작은 박자이면 -
            if beatimg == "small":
                # 작은 박자 이미지 그리기
                obj.img_beat_small.draw(startx, starty, SIZE_BEAT_SMALL_X, SIZE_BEAT_SMALL_Y)

            # 해당 박자가 큰 박자이면 - 큰 박자 이미지 그리기
            elif beatimg == "big":
                # 큰 박자 이미지 그리기
                obj.img_beat_big.draw(startx, starty, SIZE_BEAT_BIG_X, SIZE_BEAT_BIG_Y)
    pass

# 하트 및 체력바 그리기
def draw_life_hp_info(obj, p_nowlife, p_maxlife, e_nowhp, e_maxhp):
    if obj.img_info_hpbar_bg == None:
        obj.img_info_hpbar_bg = load_image('img_info_hpbar_bg.png')
    if obj.img_info_hpbar_hp == None:
        obj.img_info_hpbar_hp = load_image('img_info_hpbar_hp.png')
    if obj.img_info_hpbar_frame == None:
        obj.img_info_hpbar_frame = load_image('img_info_hpbar_frame.png')
    if obj.img_info_playerlife == None:
        obj.img_info_playerlife = load_image('img_info_playerlife.png')
    if obj.img_info_playerlife_lost == None:
        obj.img_info_playerlife_lost = load_image('img_info_playerlife_lost.png')

    if obj.img_whitesquare == None:
        obj.img_whitesquare = load_image('img_whitesquare.png')

    player_now_life, player_max_life = p_nowlife, p_maxlife # 플레이어 하트
    enemy_hp_left, enemy_hp_total = e_nowhp, e_maxhp # 적 체력

    HPBARLENGTH = 150 # 체력바 길이
    HPBARPOSY   = 450 # 체력바 y위치
    hpnow_drawlength = HPBARLENGTH * (enemy_hp_left / enemy_hp_total) # 남은 체력 길이
    hpnowposx = 400 - (HPBARLENGTH - hpnow_drawlength) / 2 # 남은 체력 현재 위치

    # 플레이어 하트 그리기
    for n in range(player_max_life):
        obj.img_whitesquare.draw(50, 50 + n * 50, 60, 60)
        obj.img_info_playerlife_lost.draw(50, 50 + n * 50, 30, 30)
    for n in range(player_now_life):
        obj.img_whitesquare.draw(50, 50 + n * 50, 60, 60)
        obj.img_info_playerlife.draw(50, 50 + n * 50, 30, 30)

    # 적 체력 그리기
    obj.img_info_hpbar_bg.draw   (400,       HPBARPOSY, HPBARLENGTH,      40)
    obj.img_info_hpbar_hp.draw   (hpnowposx, HPBARPOSY, hpnow_drawlength, 40)
    obj.img_info_hpbar_frame.draw(400,       HPBARPOSY, HPBARLENGTH,      40)

    pass