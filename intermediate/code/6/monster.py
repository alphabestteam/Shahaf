from hero import Hero

class Monster:
    def __init__(self, name) -> None:
        self.name = name
        self.hp = 10
        self.damage = 2
        self.level = 1
    
    def attack(self, hero: Hero) -> None:
        hero.reduce_health(self)

    def reduce_health(self, hero: Hero) -> int:
        self.hp = self.hp - hero.damage

        if self.hp < 0:
            self.hp = 0

        return self.hp