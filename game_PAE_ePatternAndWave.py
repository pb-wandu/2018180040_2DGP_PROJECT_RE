# ----------<대결 상대 패턴 및 Wave>----------

# 대결 상대의 패턴과 Wave를 기록한 파일
# 패턴 이미지에 보이는 대로 동일한 위치에 대응하면 됩

# <목록>
# "small" : 작은 박자. 여기서는 플레이어도 대결 상대도 공격하지 않음
# "big_p_left"  : 큰 박자. 플레이어가 왼쪽으로 공격  - 하면 유효타
# "big_p_right" : 큰 박자. 플레이어가 오른쪽으로 공격 - 하면 유효타
# "big_e_left"  : 큰 박자. 적이 왼쪽으로 공격       - 막으면 방어 성공
# "big_e_right" : 큰 박자. 적이 오른쪽으로 공격     - 막으면 방어 성공

import gamemode_2_1_gameinfo as gamestate # 게임 정보 관련 모듈 import

# 게임 볼륨 설정 (임의) : 실제 스테이지 및 웨이브 개수와 일치하지 않음
MAXSTAGENUM = 20 # 최대 스테이지 개수
MAXWAVENUM  = 10 # 최대 Wave 개수

# 실제 전체 웨이브 개수
ALLWAVENUM = 6

# ----- 동작 패턴 상세 -----

### 대결 상대 1-1 (예시)
### 큰 박자 상세 동작 추가 예정

waveEnemyPattern  = [[] for _ in range(MAXWAVENUM)]                # Wave당 대결 상대 패턴
totalEnemyPattern = [waveEnemyPattern for _ in range(MAXSTAGENUM)] # 전체 대결 상대 패턴

# ----- <적 정보> 전체 -----

# 각 스테이지당 적 수  ### 현재 숫자는 임의로 넣음
stageEnemyNum = [3, 3, 3, 3, 3, 3]

# 각 스테이지당 적 체력 ### 현재 숫자는 임의로 넣음
stageEnemyHP = [
    ### 현재 숫자는 임의로 넣음
    [50, 50, 50, 50, 0],
    [50, 50, 50, 50, 0],
    [50, 50, 50, 50, 0],
    [50, 50, 50, 50, 0],
    [50, 50, 50, 50, 0],
    [50, 50, 50, 50, 0],
]



# 패턴 수 (대결 상대 하나가 돌아가며 반복하는 패턴 수)
patternNum = [
    ### 현재 숫자는 임의로 넣음
    [2, 2, 2, 3, 0],
    [4, 4, 4, 4, 0],
    [5, 5, 5, 5, 0],
    [5, 5, 5, 5, 0],
    [5, 5, 5, 5, 0],
    [5, 5, 5, 5, 0],
]

# 박자 수 (한 패턴당 네모 수)
beatNum = [
    ### 현재 숫자는 임의로 넣음
    [4, 4, 4, 4, 0],
    [4, 4, 4, 4, 0],
    [4, 4, 4, 4, 0],
    [4, 4, 4, 4, 0],
    [4, 4, 4, 4, 0],
    [4, 4, 4, 4, 0],
]

# ----- 스테이지 이동 함수 (이전, 다음) -----

# 이전 wave로 이동
def move_prevWave():
    n_stage = gamestate.gameinfomation.nowStage # 현재 스테이지
    n_wave  = gamestate.gameinfomation.nowWave  # 현재 wave

    # 현재 wave가 해당 stage의 첫 wave일 경우
    if n_wave == 1:
        # 현재 stage가 1stage가 아닌 경우
        if n_stage != 1:
            # 이전 스테이지로 이동하고 마지막 웨이브로 지정
            gamestate.gameinfomation.nowStage -= 1
            gamestate.gameinfomation.nowWave   = stageEnemyNum[n_stage - 1]

    # 이외의 경우 이전 wave로 이동
    else:
        gamestate.gameinfomation.nowWave -= 1

# 다음 웨이브로 이동
def move_nextWave():
    n_stage = gamestate.gameinfomation.nowStage # 현재 스테이지
    n_wave  = gamestate.gameinfomation.nowWave  # 현재 wave

    # 현재 wave가 해당 stage의 마지막 wave일 경우
    if n_wave == stageEnemyNum[n_stage - 1]:

        # 현재 stage가 최종 stage가 아닌 경우
        if n_stage != ALLWAVENUM:
            # 다음 스테이지로 이동하고 1웨이브로 지정
            gamestate.gameinfomation.nowStage += 1
            gamestate.gameinfomation.nowWave   = 1

        # 현재 stage가 최종 stage인 경우
        else:
            ### 내용 추가하기 - GAME CLEAR!!!
            pass

    # 이외의 경우 다음 wave로 이동
    else:
        gamestate.gameinfomation.nowWave += 1

# ----- <적 정보> 1스테이지 -----

totalEnemyPattern[0][0] = [
    ["small", "small", "small", "big", None, None],
    ["small", "big", "small", "big", None, None],
]
totalEnemyPattern[0][1] = [
    ["small", "small", "small", "big", None, None],
    ["small", "big", "small", "big", None, None],
]
totalEnemyPattern[0][2] = [
    ["small", "small", "small", "big", None, None],
    ["small", "big", "small", "big", None, None],
]





