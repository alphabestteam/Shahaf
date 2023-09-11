from Person import Person

def main():
    for _ in range(10):
        name = input('Enter a name: ')
        id = input('Enter the id: ')
        age = int(input('Enter the age: '))

        person = Person(name, id, age)
        print(person)


if __name__ == "__main__":
    main()