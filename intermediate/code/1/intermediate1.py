import math
import random

def add_two_number(number_one = 0, number_two = 0) -> float:  #adds two numbers
    return number_one + number_two

def print_name(name: str) -> None:  #prints a greeting
    print(f'Hello {name}! Great to see u')

def quadratic_equation(a: float, b: float, c: float) -> None:  #solves a quadratic equation
    delta = (b ** 2) - (4 * a * c)

    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(a * 2)
        x2 = (-b - math.sqrt(delta))/(a * 2)
        print('x1 : ' + str(x1)+ ' x2 : ' + str(x2))

    elif delta == 0:
        x1 = (-b)/(a * 2)
        print('x1 : ' + str(x1))
        
    else:
        print('No solutions')

def random_in_range_int(number_one: int, number_two: int) -> int:  #returns a random int number
    return random.randrange(number_one, number_two)

def random_in_range_float(number_one: float, number_two: float) -> float:  #returns a random float number
    return random.uniform(number_one, number_two)

def main():
    number_one = float(input('Enter a number: '))
    number_two = float(input('Enter a number: '))
    print(str(add_two_number(number_one, number_two)))

    name = input('Enter a name: ')
    print_name(name)

    a = float(input('Enter a number: '))
    b = float(input('Enter a number: '))
    c = float(input('Enter a number: '))
    quadratic_equation(a, b, c)

    int_number_one = int(input('Enter a number: '))
    int_number_two = int(input('Enter a number: '))
    print(str(random_in_range_int(int_number_one, int_number_two)))

    float_number_one = float(input('Enter a number: '))
    float_number_two = float(input('Enter a number: '))
    print(str(random_in_range_float(float_number_one, float_number_two)))


if __name__ == "__main__":
    main()