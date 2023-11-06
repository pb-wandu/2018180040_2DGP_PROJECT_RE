# ----------<게임 충돌 체크>----------

collision_pairs = {} # 충돌 조합 저장

# 충돌 조합 추가
def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'새로운 충돌 조합 ({group}) 추가')

    # a, b를 충돌 조합의 각 위치에 추가
    collision_pairs[group] = [ [] , [] ]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

# 충돌 오브젝트 제거
def remove_collision_object(obj):
    for pairs in collision_pairs.values():
        # 오브젝트가 충돌 조합의 a, b 위치 중 있는 경우 지우기
        if obj in pairs[0]:
            pairs[0].remove(obj)
        if obj in pairs[1]:
            pairs[1].remove(obj)

# 충돌 처리
def handle_collisions():
    # collision_pairs에 있는 group과 pairs에 대하여
    for group, pairs in collision_pairs.items():
        # 오브젝트 a, b에 대하여
        for a in pairs[0]:
            for b in pairs[1]:
                # a, b가 충돌하였다면
                if collide(a, b):
                    # a.handle_collision(group, b)
                    # b.handle_collision(group, a)
                    ### 나중에 각 오브젝트에 handle_collision 넣으면 적용할 것
                    pass







