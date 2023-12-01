# ----------<사운드 관련 코드>----------

# 게임에 사용되는 사운드 관련 내용을 기록한 파일

# 공격(명중)시 음악
class Sound_hit:

    def __init__(self):
        self.sound = load_music('./resource_music/sound_hit.wav')

    def set_volume(self, n):
        self.sound.set_volume(n)

    def play(self, n):
        self.sound.play(n)

    pass

# 이동(회피)시 음악
class Sound_move:

    def __init__(self):
        self.sound = load_music('./resource_music/sound_move.wav')

    def set_volume(self, n):
        self.sound.set_volume(n)

    def play(self, n):
        self.sound.play(n)

    pass

# ----- 실제 오브젝트 -----

sound_hit  = Sound_hit()  # 공격(명중)시 음악
sound_move = Sound_move() # 이동(회피)시 음악