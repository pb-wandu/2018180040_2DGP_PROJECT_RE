# -----------<함수들>-----------

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

    # maxtime 초과시 0틱으로 초기화
    if obj.nowtick > obj.maxtick:
        obj.nowtick = 0

    ### 테스트용 - 박자 표시
    if obj.nowtick % obj.ticknum == 0 and obj.nowtick != 0:
        ### 테스트용 - 큰박자
        if obj.nowtick == obj.maxtick:
            print(f"<큰 박자> 박자표 [{obj.beatnum} / {obj.beatnum}] 박자")
        ### 테스트용 - 그 외
        else:
            print(f"박자표 [{int(obj.nowtick / obj.ticknum)} / {obj.beatnum}] 박자")

# 박자표 그리기

def draw_beattimer(obj):

    img_beat_small = load_image('img_beat_small.png')
    img_beat_big = load_image('img_beat_big.png')

    beatnum = obj.beatnum  # 박자 수

    SIZEX, SIZEY = 100, 100  # 이미지 크기
    CENTERX, CENTERY = 400, 500  # 박자표 중심

    # 박자표 이미지 list에서 - index는 list에서의 위치, beat는 실제 값
    for index, beatimg in enumerate(obj.beat_image_list):

        # 이미지 그리기 시작하는 위치
        startx = (CENTERX - (beatnum - 1) * SIZEX / 2) + (index * SIZEX)
        starty = CENTERY

        # 해당 박자가 없으면 - 그리기 종료
        if beatimg == None:
            break

        # 해당 박자가 작은 박자이면 - 작은 박자 이미지 그리기
        elif beatimg == "small":
            img_beat_small.draw(startx, starty, SIZEX, SIZEY)

        # 해당 박자가 큰 박자이면 - 큰 박자 이미지 그리기
        elif beatimg == "big":
            img_beat_big.draw(startx, starty, SIZEX, SIZEY)