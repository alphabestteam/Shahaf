import random

class Monster:
    STRONG = 0.5

    def __init__(self, name: str, level: int) -> None:
        self.name = name
        self.hp = 10 * (level * Monster.STRONG)
        self.damage = 2 * (level * Monster.STRONG)
        self.level = random.randrange(level - 1, level + 2)
    
    def attack(self, hero) -> None:
        hero.reduce_health(self)
        print(f'The monster attacked you, you have {hero.hp} lives!')

    def reduce_health(self, hero) -> int:
        self.hp = self.hp - hero.damage

        if self.hp < 0:
            self.hp = 0

        return self.hp