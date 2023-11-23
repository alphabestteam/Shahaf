class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, point) -> bool:
        if point.x == self.x and point.y == self.y:
            return True
        
        return False

    def __str__(self) -> str:
        return (f'x value is: {self.x} and y value is: {self.y}')
    
    def __add__(self, point) -> float:
        point_three = Point(self.x + point.x, self.y + point.y)
        return point_three

def main():
    point_one = Point(6, 8)
    point_two = Point(6, 8)

    print(point_one == point_two)

    print(point_one)
    print(point_two)

    print(point_one + point_two)


if __name__ == "__main__":
    main()