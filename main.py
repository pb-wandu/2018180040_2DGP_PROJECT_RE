# ----------<main 파일>----------

# 실제 실행(main) 부분 코드를 기록한 파일

from pico2d import * # pico2d 모듈 import
import game_world    # world 전체 관련 내용 모듈 import

# ----- 실제 게임 실행 부분 -----

# 화면 실행
open_canvas(800, 600)

# 초기 설정
game_world.init_world()

# 게임 진행
while game_world.gameplaying:
    # 게임 진행중 game_world의 동작
    game_world.handle_events()    # event를 입력받는다
    game_world.update_allobject() # world 안 오브젝트 전체를 업데이트한다
    game_world.render_allobject() # world 안 오브젝트 전체를 그린다

# 게임 종료
print("게임 종료 (world.gameplaying == False)")
close_canvas()
