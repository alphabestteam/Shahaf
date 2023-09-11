class Hero:
    M = 1.5
    K = 2
    N = 1.7

    def __init__(self, name) -> None:
        self.name = name
        self.hp = 10
        self.damage = 2
        self.level = 1
        self.coins = 0
        
    def heal(self) -> None: 
        self.hp = self.hp * Hero.N
        print(f'You healed yourself, now you have {self.hp} lives!')

    def level_up(self) -> None:
        if (self.coins / (self.level + 1)) >= Hero.K:
            self.hp = 10 * Hero.M
            self.damage = self.damage * Hero.M
            self.level = self.level + 1

            print(f'Leveled up! you are now in level {self.level}')

    def attack(self, monster) -> None:
        from monster import Monster
        monster_lives = monster.reduce_health(self)
        print('You attacked the monster!')

        if monster_lives == 0:
            self.coins = self.coins + self.level

    def defend(self, damage) -> float:
        return damage * 0.2

    def reduce_health(self, monster, action_history: list) -> int:
        from monster import Monster
        if len(action_history) < 2 or action_history[-2] != '4':
            self.hp = self.hp - monster.damage

        else:
            self.hp = self.hp - monster.damage
            monster.damage = monster.damage / 0.2

        if self.hp < 0:
            self.hp = 0

        return self.hp


    def increase_coins(self, number_of_coins: int) -> None:
        self.coins = self.coins + number_of_coins 