# -----------<상태들>-----------

# Idle 상태
class Idle:
    @staticmethod
    def enter(player, e):
        print("Idle enter")
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        pass

    @staticmethod
    def exit(player, e):
        print("Idle exit")
        pass