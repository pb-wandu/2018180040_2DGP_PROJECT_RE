# ----------<테스트 코드 작성용 파일>----------

# 실제 게임플레이와 관련없음

from pico2d import * # pico2d 모듈 import

# ----- '임시 플레이'용 내용 -----

# event 처리
def handle_events():
    global temp_playing # 게임 실행중 여부

    left_punch_keys = [
        SDLK_q, SDLK_w, SDLK_e, SDLK_r, SDLK_t,
        SDLK_a, SDLK_s, SDLK_d, SDLK_f, SDLK_g,
        SDLK_z, SDLK_x, SDLK_c, SDLK_v, SDLK_b
    ]
    right_punch_keys = [
        SDLK_i, SDLK_o, SDLK_p, SDLK_LEFTBRACKET, SDLK_RIGHTBRACKET,
        SDLK_j, SDLK_k, SDLK_l, SDLK_SEMICOLON, SDLK_QUOTE,
        SDLK_n, SDLK_m, SDLK_COMMA, SDLK_PERIOD, SDLK_SLASH
    ]

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
    update_canvas() # 화면 업데이트

# 게임 종료
print("게임 종료 (temp_playing == False)")
close_canvas()