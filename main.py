# ----------<main 파일>----------

# 실제 실행(main) 부분 코드를 기록한 파일

from pico2d import * # pico2d 모듈

from statemachine_and_objects import * # 상태 머신 및 동작들을 담은 모듈
import world # world 전체 관련 내용을 담은 모듈

### [1주차 할 일] ###
### 박자표 구현 및 게임 흐름 ###

# ----- 실제 게임 실행 부분 -----

# 화면 실행
open_canvas()

# 초기 설정
world.init_world()

# 게임 진행
while world.gameplaying:

    world.handle_events() # event를 입력받는다
    world.update_world()  # world를 업데이트한다
    world.render_world()  # world를 그린다

    delay(0.01) # 동작 사이 지연 시간

# 게임 종료
close_canvas()
