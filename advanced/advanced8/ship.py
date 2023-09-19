class Ship:
    def __init__(self, position: str, start: dict, end: dict, lives: int) -> None:
        self.position = position
        self.start = start
        self.end = end
        self.lives = lives