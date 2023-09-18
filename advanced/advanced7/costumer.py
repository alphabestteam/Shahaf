from product import Product

class Costumer:

    def __init__(self, name: str) -> None:
        self.costumer_name = name
        self.shopping_list = []
        self.list_total_price = 0

    def add_product(self, product: Product) -> None:
        is_exist = False

        for item in self.shopping_list:
            if item.name_of_product == product.name_of_product:
                is_exist = True
                self.list_total_price = self.list_total_price - item.total_price + self.product.total_price
                units = product.units
                self.shopping_list.pop(self.shopping_list.index(item))
                product.units = units
                product.total_price = units * product.price_of_item
                self.shopping_list.append(product)
                print('Item was updated!') 

            elif is_exist:
                break
        
        if not is_exist:
            self.shopping_list.append(product)
            self.list_total_price = self.list_total_price + product.total_price
            print('Item was added')


    def remove_product(self, name: str, units_to_remove: int) -> None:
        is_exist = False

        for item in self.shopping_list:
            if item.name_of_product == name:
                is_exist = True
                if item.units > units_to_remove:
                    units = item.units - units_to_remove
                    self.list_total_price = self.list_total_price - item.total_price + (item.price_of_item * units)
                    name = item.name_of_product
                    price = item.price_of_item
                    total_price = item.total_price - (price * item.units) + (price * units)
                    product = Product(name, price, units, total_price)
                    self.shopping_list.pop(self.shopping_list.index(item))
                    self.shopping_list.append(product)
                    print('Item was updated!') 

                elif item.units == units_to_remove:
                    self.list_total_price = self.list_total_price - item.total_price
                    self.shopping_list.pop(self.shopping_list(self.shopping_list.index(item)))
                    print('Item was removed')

                else:
                    print('Requested amount cant be removed!')

            elif is_exist:
                break
        
        if not is_exist:
            print('Item does not exist!')        