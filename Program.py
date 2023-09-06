import math

def factorial(number: float) -> float:
    return math.factorial(number)

def main():
    sum_1_to_100 = 0
    for number in range(1, 101):
        sum_1_to_100 = sum_1_to_100 + number

    print(str(sum_1_to_100))

    print(factorial(6.5))
    print(factorial(7))
    print(factorial(8))

if __name__ == "__main__":
    main()