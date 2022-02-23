class GameInfo:

    def __init__(self):
        self.passed_pipes = 0
        self.alive = True

    def reset(self):
        self.passed_pipes = 0
        self.alive = True
