# ----------<대결 상대 패턴 및 Wave>----------

# 대결 상대의 패턴과 Wave를 기록한 파일
# 패턴 이미지에 보이는 대로 동일한 위치에 대응하면 됩

# <목록>
# "small" : 작은 박자. 여기서는 플레이어도 대결 상대도 공격하지 않음
# "big_p_left"  : 큰 박자. 플레이어가 왼쪽으로 공격  - 하면 유효타
# "big_p_right" : 큰 박자. 플레이어가 오른쪽으로 공격 - 하면 유효타
# "big_e_left"  : 큰 박자. 적이 왼쪽으로 공격       - 막으면 방어 성공
# "big_e_right" : 큰 박자. 적이 오른쪽으로 공격     - 막으면 방어 성공

# 게임 볼륨 설정 (임의)
MAXSTAGENUM = 20 # 최대 스테이지 개수
MAXWAVENUM  = 5  # 최대 Wave 개수

# ----- 동작 패턴 상세 -----

### 대결 상대 1-1 (예시)
### 큰 박자 상세 동작 추가 예정

waveEnemyPattern  = [[] for _ in range(MAXWAVENUM)]                # Wave당 대결 상대 패턴
totalEnemyPattern = [waveEnemyPattern for _ in range(MAXSTAGENUM)] # 전체 대결 상대 패턴

totalEnemyPattern[0][0] = [
    ["small", "small", "small", "big", None, None],
    ["small", "small", "big", "small", None, None],
    ["small", "big", "small", "big", None, None],
]

# 패턴 수
patternNum = [
    ### 현재 숫자는 임의로 넣음
    [3, 3, 3, 3, 0],
    [4, 4, 4, 4, 0],
    [5, 5, 5, 5, 0],
    [0, 0, 0, 0, 0],
]





