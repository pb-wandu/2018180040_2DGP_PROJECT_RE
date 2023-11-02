# ----------<테스트 코드 작성용 파일>----------

# 실제 게임플레이와 관련없음

from pico2d  import * # pico2d 모듈 import

# ----- '임시 플레이'용 내용 -----

# event 처리
def handle_events():
    global temp_playing # 게임 실행중 여부

    events = get_events() # event 입력받기

    # 입력받은 event에 따라
    for event in events:

        # SDL_QUIT 또는 Esc키 누를 시 게임 플레이 종료
        if event.type == SDL_QUIT:
            temp_playing = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            temp_playing = False

        # 왼쪽 5줄 / 오른쪽 5줄로 각각 왼쪽 / 오른쪽 펀치
        elif event.type == SDL_KEYDOWN and event.key in left_punch_keys:
            print("왼쪽 펀치 -", event.type)
        elif event.type == SDL_KEYDOWN and event.key in right_punch_keys:
            print("오른쪽 펀치 -", event.key)

    pass

# ----- '임시 화면' 실행 -----

open_canvas(800, 600)

temp_playing = True

# 게임 진행
while temp_playing:
    clear_canvas()  # 화면 초기화
    handle_events() # 동작 핸들러

    # 여기다가 입력

    img_info_hpbar_bg = load_image('img_info_hpbar_bg.png')
    img_info_hpbar_hp = load_image('img_info_hpbar_hp.png')
    img_info_hpbar_frame = load_image('img_info_hpbar_frame.png')
    img_info_playerlife = load_image('img_info_playerlife.png')
    img_info_playerlife_lost = load_image('img_info_playerlife_lost.png')

    HPBARLENGTH = 150

    enemy_hp_total = 100
    enemy_hp_left = 70

    player_max_life = 3
    player_life_now = 2

    for n in range(player_max_life):
        img_info_playerlife_lost.draw(140 + n * 60, 200, 40, 40)
    for n in range(player_life_now):
        img_info_playerlife.draw(140 + n * 60, 200, 40, 40)

    hpbar_drawlength = HPBARLENGTH * (enemy_hp_left / enemy_hp_total)

    img_info_hpbar_bg.draw(100, 500, HPBARLENGTH, 40)
    img_info_hpbar_hp.draw(100 - (HPBARLENGTH - hpbar_drawlength)/2, 500, hpbar_drawlength, 40)
    img_info_hpbar_frame.draw(100, 500, HPBARLENGTH, 40)

    # 시간
    nowgametime = get_time()

    font = load_font('ENCR10B.TTF', 16)
    font.draw(100, 100, f'(Time: {nowgametime:.2f})', (0, 0, 0))

    # 여기다가 입력 종료

    update_canvas() # 화면 업데이트

# 게임 종료
print("게임 종료 (temp_playing == False)")
close_canvas()