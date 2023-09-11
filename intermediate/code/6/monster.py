class Monster:
    def __init__(self, name) -> None:
        self.name = name
        self.hp = 10
        self.damage = 2
        self.level = 1
    
    def attack(self, hero, action_history: list) -> None:
        from hero import Hero
        hero.reduce_health(self, action_history)
        print(f'The monster attacked you, you have {hero.hp} lives!')

    def reduce_health(self, hero) -> int:
        from hero import Hero
        self.hp = self.hp - hero.damage

        if self.hp < 0:
            self.hp = 0

        return self.hp