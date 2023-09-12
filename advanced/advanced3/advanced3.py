import time

class Person:
    def __init__(self, name_list: list) -> None:
        self.name_list = name_list

    def AddPerson(self, name: str) -> None:
        self.name_list.append(name)

def timer(func: function) -> None:
     before = time.time()

     func()

     after = time.time()

     print(f'The function run time was {after - before} seconds')

def main():

    name_list = Person(['shahaf', 'shoham', 'yotam'])
    iter_name_list = iter(name_list.name_list)
    print(next(iter_name_list))
    print(next(iter_name_list))

if __name__ == '__main__':
    main()