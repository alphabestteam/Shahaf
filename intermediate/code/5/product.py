class Product:

    def __init__(self, name: str, price: float, units: int, total_price: float) -> None:
        self.name_of_product = name
        self.price_of_item = price
        self.units = units
        self.total_price = total_price

    def print_item(self) -> None:
        print(f'The name of the product: {self.name_of_product}')
        print(f'The price of the product: {self.price_of_item}')
        print(f'The number of units: {self.units}')
        print(f'The total price: {self.total_price}')