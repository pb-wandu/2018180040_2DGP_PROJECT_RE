# -----------<동작 함수들>-----------

# 이벤트 및 오브젝트별 동작 함수를 기록한 파일

from pico2d import * # pico2d 모듈 import
# import images      # 이미지 저장 모듈 import

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
        player.nowpunchhand = "right"
    else: # 다른 키를 눌렀다면
        player.nowpunchhand = None
    """
    return False  ### 임시


# 박자표 - 시간 업데이트 (1틱 간격)
def timeupdate(obj):
    # nowtime 1틱씩 진행
    obj.nowtick += 1

    # 최대 틱(에서 100틱) 초과시 0틱으로 초기화
    if obj.nowtick > (obj.maxtick + 100):
        obj.nowtick = 0

    ### 테스트용 - 박자 표시
    if obj.nowtick % obj.ticknum == 0 and obj.nowtick != 0:
        ### 테스트용 - 큰박자
        if obj.nowtick == (obj.maxtick + 100):
            print(f"<큰 박자> 박자표 [{obj.beatnum} / {obj.beatnum}] 박자")
        ### 테스트용 - 그 외
        else:
            print(f"박자표 [{int(obj.nowtick / obj.ticknum)} / {obj.beatnum}] 박자")

# 박자표 그리기

def draw_beattimer(obj):

    img_beat_bg     = load_image('img_beat_bg.png')     # 박자 배경
    img_beat_effect = load_image('img_beat_effect.png') # 현재 박자 이펙트
    img_beat_small  = load_image('img_beat_small.png')  # 작은 박자
    img_beat_big    = load_image('img_beat_big.png')    # 큰 박자

    beatnum = obj.beatnum  # 박자 수

    SIZE_BG_X, SIZE_BG_Y                 = 100, 100 # 박자표 틀 이미지 크기
    SIZE_EF_X, SIZE_EF_Y                 = 90, 90   # 박자표 효과 이미지 크기
    SIZE_BEAT_BIG_X, SIZE_BEAT_BIG_Y     = 70, 70   # 큰 박자 이미지 크기
    SIZE_BEAT_SMALL_X, SIZE_BEAT_SMALL_Y = 40, 40   # 작은 박자 이미지 크기

    CENTERX, CENTERY = 400, 500 # 박자표 중심

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