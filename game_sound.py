# ----------<사운드 관련 코드>----------

from pico2d import * # pico2d 모듈 import

# 게임에 사용되는 사운드 관련 내용을 기록한 파일

# 공격(명중)시 사운드
class Sound_hit:
    sound = None

    def __init__(self):
        if not Sound_hit.sound:
            Sound_hit.sound = load_wav('./resource_sound/sound_hit.wav')

    def set_volume(self, n):
        self.sound.set_volume(n) # 0 ~ 128

    def play(self):
        self.sound.play(1)

    pass

# 이동(회피)시 사운드
class Sound_move:
    sound = None

    def __init__(self):
        if not Sound_move.sound:
            Sound_move.sound = load_wav('./resource_sound/sound_move.wav')

    def set_volume(self, n):
        self.sound.set_volume(n) # 0 ~ 128

    def play(self):
        self.sound.play(1)

    pass