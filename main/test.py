class ScreenImages:
    def __init__(self):
        print("Initializing ScreenImages")

class GameMusic:
    def __init__(self):
        print("Initializing GameMusic")

class GameScreen(ScreenImages, GameMusic):
    def __init__(self):
        super().__init__()  # 调用 MRO 中的第一个基类
        print("Initializing GameScreen")

# 测试
gs = GameScreen()