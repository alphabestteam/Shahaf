def is_prime(number_is_prime: int) -> None:
    is_prime = True
    for number in range(2, number_is_prime):
        if number_is_prime % number == 0:
            is_prime = False
            break

    if is_prime == True:
        print(f'{number_is_prime} is a prime number')

    else:
        print(f'{number_is_prime} is not a prime number')

def main():
    sum_1_to_100 = 0
    for number in range(100):
        sum_1_to_100 = sum_1_to_100 + number

    print(str(sum_1_to_100))

    is_prime(5)
    is_prime(6)
    is_prime(7)
    is_prime(14)
    is_prime(152)
    is_prime(60693)

if __name__ == "__main__":
    main()