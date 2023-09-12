import time

class Person:
    def __init__(self, name_list: list) -> None:
        self.name_list = name_list

    def AddPerson(self, name: str) -> None:
        self.name_list.append(name)

def timer(func) -> None:
     before = time.time()

     func()

     after = time.time()

     print(f'The function run time was {after - before} seconds')

def hello() -> None:
    print('Hello')

def N_series(N: int) -> int:
    series = [1, 2]
    yield 1
    yield 2

    if N > 2:
        for index in range(3, N + 1):
            yield series[index-1-1] * series[index-2-1]

def main():
    run_time = timer(hello)
    
    name_list = Person(['shahaf', 'shoham', 'yotam'])
    iter_name_list = iter(name_list.name_list)
    print(next(iter_name_list))
    print(next(iter_name_list))

    N = int(input("Enter requested number of items: "))
    series = N_series(N)
    for item in series:
        print(item)


if __name__ == '__main__':
    main()