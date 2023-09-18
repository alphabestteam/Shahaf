from ship import Ship

class Submarine(Ship):
    def __init__(self, position: str, start: str, end: str) -> None:
        Ship.__init__(self, position: str, start: str, end: str),
        super().__init__(position: str, start: str, end: str),
        self.length = 3