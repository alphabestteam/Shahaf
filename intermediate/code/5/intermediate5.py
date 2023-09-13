from product import Product
from costumer import Costumer
from register import Register
import os
import json

def main():
    register_list = []

    while True:
        print('Enter 1 to add a new register')  #prints action menu
        print('Enter 2 to use last created register')
        print('Enter 3 to finish')
        action = input('Enter your requested action: ')

        if action == '1':
            register = Register()
            register_list.append(register)
            print('register was created!')

        elif action == '2':
            register = register_list[-1]

            name = input('Enter the name: ')
            costumer = Costumer(name)

            while True:
                print('Enter 1 to add an item')  #prints action menu
                print('Enter 2 to remove an item')
                print('Enter 3 to exit')
                action = input('Enter your requested action: ')

                if action == '1':
                    name = input('Enter the name of the item: ')
                    cost = float(input('Enter the cost of the item: '))
                    quantity = int(input('Enter the quantity: '))
                    item = Product(name, cost, quantity, (cost * quantity))
                    costumer.add_product(item)

                    with open(f'./items/{name}.json', 'w') as file:
                        json.dump({'name': name, 'price': cost, 'units': quantity}, file)

                elif action == '2':
                    name = input('Enter the name of the item: ')
                    quantity = int(input('Enter the quantity to remove: '))
                    costumer.remove_product(name, quantity)

                elif action == '3':
                    with open(f'{costumer.costumer_name}.json', 'w') as file:
                        shopping_dict = {}
                        for item in costumer.shopping_list:
                            name_of_item = item.name_of_product
                            price = item.price_of_item
                            units = item.units
                            total_price = item.total_price
                            shopping_dict.update({'name': name_of_item, 'price': price, 'units': units, 'total price': total_price})
                        json.dump({costumer.costumer_name: shopping_dict}, file)

                    register.checkout_costumer(costumer)
                    print(f'Thank you for shopping {name}')
                    break

                else:
                    print('Invalid value')

        elif action == '3':
            for number_of_register in range(len(register_list)):
                print(f'Description for register number {number_of_register + 1}:')
                print(register.print_summery())
            break

        else:
            print('Invalid value')

    print('Registers are not active')


if __name__ == "__main__":
    main()