from Person import Person

def print_two_numbers(number_one:str, number_two:str) -> None:
    try:
        print(f'first number: {number_one} second number: {number_two}')

    except TypeError:
        print(f'first number: {str(number_one)} second number: {str(number_two)}')

    print('Finished running')

def quadric_list() -> None:
    N = int(input('Enter a number: '))
    quadric_list = [number ** 2 for number in range(N)]
    print(quadric_list)

def person_list() -> None:
    N = int(input('Enter a number: '))
    person_list = [Person(name = input('Enter a name: '), id = input('Enter the id: '), age = int(input('Enter the age: '))) for person in range(N)]
    older_than_18 = []
    for person in person_list:
        if person.age > 18:
            older_than_18.append(person)
            print(person)

def main():
    number_one = input('Enter a number: ')
    number_two = input('Enter a number: ')
    print_two_numbers(number_one, number_two)

    quadric_list()

    person_list()


if __name__ == "__main__":
    main()