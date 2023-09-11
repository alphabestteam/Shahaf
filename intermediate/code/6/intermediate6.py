from hero import Hero
from monster import Monster

def choose_action(action: str, hero: Hero, monster: Monster) -> None:
    if action == '1':
        hero.attack(monster)

    elif action == '2':
        hero.level_up()

    elif action == '3':
        hero.heal()

    elif action == '4':
        monster.damage = hero.defend(monster.damage)

    else:
        print('Invalid value!')

def main():
    name_hero = input('Enter the name of the hero: ')
    name_monster = input('Enter the name of the monster: ')

    hero = Hero(name_hero)
    monster = Monster(name_monster)

    action_history_hero = []

    turn = 1

    while hero.hp > 0:

        if turn % 2 != 0:
            print('To attack enter 1')  #prints action menu
            print('To level up enter 2')
            print('To heal enter 3')
            print('To defend enter 4')

            action = input('Enter your desirable action: ')
            action_history_hero.append(action)
            choose_action(action, hero, monster)

            hero.increase_coins(1)

        else:
            monster.attack(hero, action_history_hero)  #monster turn

        if monster.hp == 0:  #if the monster dies, create a new one
            name_monster = input('To create a new monster enter the name of the monster: ')
            monster = Monster(name_monster)

        turn = turn + 1

    print('End of the game, no more lives!')


if __name__ == "__main__":
    main()