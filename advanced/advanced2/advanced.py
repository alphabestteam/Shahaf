def words_length(*words) -> None:
    sum_length = 0

    for item in words:
        sum_length = sum_length + len(item)

    print(f'The total length is {sum_length}')

def total_age(**ages):
    sum_ages = 0

    for key, value in ages.items():
        sum_ages = sum_ages + value
        print(f'The name is {key} and the age is {value}')

    print(f'The total sum of the ages is {sum_ages}')

def main():

if __name__ == '__main__':
    main()