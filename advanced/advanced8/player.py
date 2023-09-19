from ship import Ship

class Player:
    def __init__(self) -> None:
        self.ship_positions = []
        self.ocean_grid = [['-', '-', '-', '-','-', '-', '-', '-'], 
                           ['-', '-', '-', '-','-', '-', '-', '-'], 
                           ['-', '-', '-', '-','-', '-', '-', '-'], 
                           ['-', '-', '-', '-','-', '-', '-', '-'], 
                           ['-', '-', '-', '-','-', '-', '-', '-'], 
                           ['-', '-', '-', '-','-', '-', '-', '-'], 
                           ['-', '-', '-', '-','-', '-', '-', '-'], 
                           ['-', '-', '-', '-','-', '-', '-', '-']]
        self.target_list = []
        self.hits = 0

    def sink_ship(self, ship: Ship):
        self.ship_positions.pop(self.ship_positions.index(ship))

        if ship.position == 'horizontal':
            row = ord(ship.start['letter']) - ord('a') + 1

            for index in range(ship.start['number'], ship.start['number'] + 1):
                self.ocean_grid[row][index] = '-'

        elif ship.position == 'vertical':
            column = ship.start['number']

            for row in range((ship.start['letter'] - ord('a') + 1), (ship.start['letter'] - ord('a') + 1) + 1):
                self.ocean_grid[row][column] = '-'

    def print_ocean_grid(self) -> None:
        for row in self.ocean_grid:
            print(row)

    def add_ship(self, ship: Ship) -> None:
        self.ship_positions.append(ship)

        if ship.position == 'horizontal':
            row = ord(ship.start['letter']) - ord('a') + 1

            for index in range(ship.start['number'], ship.start['number'] + 1):
                self.ocean_grid[row][index] = ship

        elif ship.position == 'vertical':
            column = ship.start['number']

            for row in range((ship.start['letter'] - ord('a') + 1), (ship.start['letter'] - ord('a') + 1) + 1):
                self.ocean_grid[row][column] = ship