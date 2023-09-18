from costumer import Costumer

class Register:

    def __init__(self) -> None:
        self.total_profit = 0
        self.total_sales_list = []

    def checkout_costumer(self, costumer: Costumer) -> None:
        self.total_profit = self.total_profit + costumer.list_total_price
        self.total_sales_list.append(costumer.shopping_list)

    def print_summery(self) -> None:
        print(f'The total profits are: {self.total_profit}')
        print('The total sales list: ')
        for shopping_list in self.total_sales_list:
            for item in shopping_list:
                item.print_item()