import json

def print_and_write() -> None:
    with open('my_file.rtf', 'r') as file:
        for each in file:
            print(each)

    with open('my_file.rtf', 'w') as file:
        file.write(input('Enter text: '))

def config_file() -> None:
    file = open('config.txt', 'r')
    lines = file.readlines()

    line_list = []
    for line in lines:
        line_data = line.split(' = ')
        line_list.append(line_data)

    data = line_list[0][1]
    silent = line_list[1][1]

    if silent == 'True':
        print(data)

    data = data.upper()

    with open('data_file.txt', 'w') as file:
        file.write(data)

def json_file() -> None:
    name = input('Enter the name: ')
    age = int(input('Enter the age: '))
    city = input('Enter the city: ')

    person_file = json.dumps({'name': name, 'age': age, 'city': city})

    person_dict = json.loads(person_file)

    print(person_dict)

    person_dict.update({'name': 'Shahaf', 'age': 18, 'city': 'netaim'})

    my_person_file = json.dumps(person_dict)

def main():
    print_and_write()

    config_file()

    json_file()


if __name__ == "__main__":
    main()