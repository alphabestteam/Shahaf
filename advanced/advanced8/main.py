from player import Player
from ship import Ship

def is_no_ship(player: Player, letter_start: str, number_start: str, letter_end: str, number_end: str) -> bool:
    if letter_start == letter_end:

        row = ord(letter_start) - ord('a') + 1

        for place in range(number_start, number_end + 1):
            if player.ocean_grid[row][place] == 'x':
                return False
            
    elif number_start == number_end:
        column = number_start

        for row in player.ocean_grid:
            if player.ocean_grid[row][column] == 'x':
                return False
            
    return True

def turn(player1: Player, player2: Player) -> None:
    letter = input('Please enter the letter of the requested shot location')
    number = input('Please enter the number of the requested shot location')

    if letter.isalpha() and number.isnumeric() and 'a' <= letter <= 'g' and '1' <= number <= '8':
        if player2[ord(letter) - ord('a') + 1][number] != '-':
            if player2[ord(letter) - ord('a') + 1][number].lives > 0:
                player2[ord(letter) - ord('a') + 1][number].lives -= 1
                print('It is a hit!')

            else:
                player2.hits += 1
                player2.sink_ship(player2[ord(letter) - ord('a') + 1][number])

        else:
            print('It is a miss!')

def main():
    for _ in range(2):
        player_one = Player()
        ships = 0
        ships_length = [5, 4, 3, 3, 2]
        while ships < 5:
            letter_start = input('Please enter the start letter of the requested placement: ')
            number_start = input('Please enter the start number of the requested placement: ')
            
            letter_end = input('Please enter the end letter of the requested placement: ')
            number_end = input('Please enter the end number of the requested placement: ')
            if ((ord(letter_end) - ord(letter_start) + 1) or (number_end - number_start + 1)) in ships_length:
                if letter_start == letter_end and str(number_end - number_start + 1) in ships_length:
                    length = number_end - number_start + 1

                elif number_start == number_end and str(ord(letter_end) - ord(letter_start) + 1) in ships_length:
                    length = ord(letter_end) - ord(letter_start) + 1

                else:
                    print('Invalid values, please try again!')
                    continue

                if 'a' <= letter_start <= 'g' and 'a' <= letter_end <= 'g' and '1' <= number_start <= '8' and '1' <= number_end <= '8':
                    if letter_start == letter_end:
                        start = {'letter': letter_start, 'number': number_start}
                        end = {'letter': letter_end, 'number': number_end}

                        if is_no_ship(player_one, letter_start, number_start, letter_end, number_end):

                            ship = Ship('horizontal', start, end, length)
                            player_one.ship_positions.append(ship)
                            player_one.add_ship(ship)
                            ships_length.pop(ships_length.index(length))
                            ships += 1
                            print('Ship was added')
                            continue

                    elif number_start == number_end:
                        start = {'letter': letter_start, 'number': number_start}
                        end = {'letter': letter_end, 'number': number_end}

                        if is_no_ship(player_one, letter_start, number_start, letter_end, number_end):

                            ship = Ship('vertical', start, end, length)
                            player_one.ship_positions.append(ship)
                            player_one.add_ship(ship)
                            ships_length.pop(ships_length.index(length))
                            ships += 1
                            print('Ship was added')
                            continue

                else:
                    print('Invalid values, please try again!')
                    continue

            print('Invalid values, please try again!')

        player_one.print_ocean_grid()

        player_two = Player()
        ships = 0
        ships_length = [5, 4, 3, 3, 2]
        while ships < 5:
            letter_start = input('Please enter the start letter of the requested placement: ')
            number_start = input('Please enter the start number of the requested placement: ')
            
            letter_end = input('Please enter the end letter of the requested placement: ')
            number_end = input('Please enter the end number of the requested placement: ')
            if ((ord(letter_end) - ord(letter_start) + 1) or (number_end - number_start + 1)) in ships_length:
                if letter_start == letter_end and str(number_end - number_start + 1) in ships_length:
                    length = number_end - number_start + 1

                elif number_start == number_end and str(ord(letter_end) - ord(letter_start) + 1) in ships_length:
                    length = ord(letter_end) - ord(letter_start) + 1

                else:
                    print('Invalid values, please try again!')
                    continue

                if 'a' <= letter_start <= 'g' and 'a' <= letter_end <= 'g' and '1' <= number_start <= '8' and '1' <= number_end <= '8':
                    if letter_start == letter_end:
                        start = {'letter': letter_start, 'number': number_start}
                        end = {'letter': letter_end, 'number': number_end}

                        if is_no_ship(player_two, letter_start, number_start, letter_end, number_end):

                            ship = Ship('horizontal', start, end, length)
                            player_one.ship_positions.append(ship)
                            player_one.add_ship(ship)
                            ships_length.pop(ships_length.index(length))
                            ships += 1
                            print('Ship was added')
                            continue

                    elif number_start == number_end:
                        start = {'letter': letter_start, 'number': number_start}
                        end = {'letter': letter_end, 'number': number_end}

                        if is_no_ship(player_two, letter_start, number_start, letter_end, number_end):

                            ship = Ship('vertical', start, end, length)
                            player_one.ship_positions.append(ship)
                            player_one.add_ship(ship)
                            ships_length.pop(ships_length.index(length))
                            ships += 1
                            print('Ship was added')
                            continue

                    else:
                        print('Invalid values, please try again!')
                        continue

            print('Invalid values, please try again!')

        player_two.print_ocean_grid()

    
    while player_one.hits > 5 and player_two.hits > 5:

        turn(player_one, player_two)
        turn(player_two, player_one)

        if player_one.hits == 5:
            print('Player 2 won!')
            break

        elif player_two.hits == 5:
            print('Player 1 won!')
            break


if __name__ == '__main__':
    main()