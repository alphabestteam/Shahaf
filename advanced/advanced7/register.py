from costumer import Costumer
import socket
from API import connect_new_account, connect_transfer

class Register:

    def __init__(self, account_number: str, balance: str) -> None:
        self.total_profit = 0
        self.total_sales_list = []
        self.account_number = account_number
        self.balance = balance

        if self.account_number == '0':
            HOST = '127.0.0.1'
            PORT = 12346

            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((HOST, PORT))
            server_socket.listen()
            print(f'listening on {HOST} on port {PORT}')

            connect_new_account()

    def checkout_costumer(self, costumer: Costumer) -> None:
        self.total_profit = self.total_profit + costumer.list_total_price
        self.total_sales_list.append(costumer.shopping_list)

        HOST = '127.0.0.1'
        PORT = 12346

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f'listening on {HOST} on port {PORT}')

        connect_transfer(self.account_number)

    def print_summery(self) -> None:
        print(f'The total profits are: {self.total_profit}')
        print('The total sales list: ')
        for shopping_list in self.total_sales_list:
            for item in shopping_list:
                item.print_item()