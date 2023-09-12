import time

def timer(func: function) -> None:
    before = time.time()

    func()

    after = time.time()

    print(f'The function run time was {after - before} seconds')

def main():

if __name__ == '__main__':
    main()