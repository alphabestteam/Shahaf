import socket, os, random, json
from client import Client

class Bank:
    def __init__(self) -> None:
        self.clients_list = []

        dir_path = '/Users/shahafgressel/Documents/צה״ל/הכשרה - git/Shahaf/advanced/advanced 6/costumers'
        dir_list = os.listdir(dir_path)

        for file in dir_list:
            file_path = (f'{dir_path}/{file}')
            client = Client(file_path)
        
            self.clients_list.append(client)

    def start_listen(self) -> None:
        HOST = '127.0.0.1'
        PORT = 12345

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f'listening on {HOST} on port {PORT}')

        menu = 'To create a new account enter 1 \nTo deposit or withdraw money enter 2 \nTo transfer money enter 3'

        while True:
            conn, addr = server_socket.accept()

            conn.sendall(menu.encode('utf-8'))
            action = conn.recv(1024).decode('utf-8')

            if action == '1':  #adds new account
                self.create_new_account(conn)

            elif action == '2':
                answer = conn.recv(1024).decode('utf-8')

                if answer == '1':
                    self.deposit(conn)

                elif answer == '2':
                    self.withdraw(conn)

                else:
                    conn.sendall('Invalid value!'.encode('utf-8'))

            elif action == '3':
                self.transfer_money(conn)

            else:
                conn.sendall('Invalid value!'.encode('utf-8'))

    def create_new_account(self, conn) -> None:
        name = conn.recv(1024).decode('utf-8')
        balance = conn.recv(1024).decode('utf-8')
                
        while True:  #finds random account number
            account_number = random.randrange(1111, 9999)
            is_exist = False

            for client in self.clients_list:
                if client.account_number == account_number:
                    is_exist = True
                    break

            if not is_exist:
                break
                
        dir_path = dir_path = '/Users/shahafgressel/Documents/צה״ל/הכשרה - git/Shahaf/advanced/advanced 6/costumers' #creates a file for new account
        with open(f'{dir_path}/{account_number}.json', 'w') as file:
            account_dir = {'name': name, 'account_number': account_number, 'balance': balance}
            file.write(json.dumps(account_dir))

        new_client = Client(f'{dir_path}/{account_number}.json')

        self.clients_list.append(new_client)

        conn.sendall(f'New account number {account_number} created successfully!'.encode('utf-8'))

    def deposit(self, conn) -> None:
        conn.sendall('Please enter the name of the client: '.encode('utf-8'))
        name = conn.recv(1024).decode('utf-8')
        conn.sendall('Please enter the account number: '.encode('utf-8'))
        account_number = conn.recv(1024).decode('utf-8')
        conn.sendall('Please enter the amount to deposit: '.encode('utf-8'))
        to_deposit= conn.recv(1024).decode('utf-8')
        is_exist = False

        for account in self.clients_list:
            if account.name == name and str(account.account_number) == str(account_number):
                is_exist = True
                account.balance = int(account.balance)+ int(to_deposit)
                self.clients_list.pop(self.clients_list.index(account))
                self.clients_list.append(account)

                dir_path = dir_path = '/Users/shahafgressel/Documents/צה״ל/הכשרה - git/Shahaf/advanced/advanced 6/costumers'  #updates the json file
                with open(f'{dir_path}/{account.account_number}.json', 'w') as file:
                    account_dir = {'name': account.name, 'account_number': account.account_number, 'balance': account.balance}
                    file.write(json.dumps(account_dir))

                conn.sendall(f'You have transfer {to_deposit} ILS'.encode('utf-8'))

        if not is_exist:
            conn.sendall('No such account!'.encode('utf-8'))

    def withdraw(self, conn) -> None:
        conn.sendall('Please enter the name of the client: '.encode('utf-8'))
        name = conn.recv(1024).decode('utf-8')
        conn.sendall('Please enter the account number: '.encode('utf-8'))
        account_number = conn.recv(1024).decode('utf-8')
        conn.sendall('Please enter the amount to withdraw: '.encode('utf-8'))
        to_withdraw = conn.recv(1024).decode('utf-8')
        is_exist = False

        for account in self.clients_list:
            if account.name == name and str(account.account_number) == str(account_number):
                is_exist = True
                account.balance = int(account.balance) - int(to_withdraw)
                self.clients_list.pop(self.clients_list.index(account))
                self.clients_list.append(account)

                dir_path = dir_path = '/Users/shahafgressel/Documents/צה״ל/הכשרה - git/Shahaf/advanced/advanced 6/costumers'  #updates the json file
                with open(f'{dir_path}/{account.account_number}.json', 'w') as file:
                    account_dir = {'name': account.name, 'account_number': account.account_number, 'balance': account.balance}
                    file.write(json.dumps(account_dir))

                conn.sendall(f'You have withdraw {to_withdraw} ILS'.encode('utf-8'))

        if not is_exist:
            conn.sendall('No such account!'.encode('utf-8'))

    def transfer_money(self, conn) -> None:
        conn.sendall('Please enter the name of the client: '.encode('utf-8'))
        sender_name = conn.recv(1024).decode('utf-8')
        conn.sendall('Please enter the account number: '.encode('utf-8'))
        sender_account_number = conn.recv(1024).decode('utf-8')
        conn.sendall('Please enter the amount to transfer: '.encode('utf-8'))
        to_transfer = conn.recv(1024).decode('utf-8')
        conn.sendall('Please enter the name of the client: '.encode('utf-8'))
        name = conn.recv(1024).decode('utf-8')
        conn.sendall('Please enter the account number: '.encode('utf-8'))
        account_number = conn.recv(1024).decode('utf-8')
        is_exist = False
        sender_is_exist = False
        account_of_sender = ''
        account_transfer = ''

        for account in self.clients_list:
            for sender_account in self.clients_list:
                if sender_account.name == sender_name and str(sender_account.account_number) == str(sender_account_number):
                    sender_is_exist = True
                    account_of_sender = sender_account

            if account.name == name  and str(account.account_number) == str(account_number):
                is_exist = True
                account_transfer = account

        if is_exist and sender_is_exist:
            account_of_sender.balance = int(account_of_sender.balance) - int(to_transfer)
            self.clients_list.pop(self.clients_list.index(account_of_sender))
            self.clients_list.append(account_of_sender)

            dir_path = dir_path = '/Users/shahafgressel/Documents/צה״ל/הכשרה - git/Shahaf/advanced/advanced 6/costumers'  #updates the json file
            with open(f'{dir_path}/{account_of_sender.account_number}.json', 'w') as file:
                account_dir = {'name': account_of_sender.name, 'account_number': account_of_sender.account_number, 'balance': account_of_sender.balance}
                file.write(json.dumps(account_dir))

            account.balance = int(account_transfer.balance) + int(to_transfer)
            self.clients_list.pop(self.clients_list.index(account_transfer))
            self.clients_list.append(account_transfer)

            dir_path = dir_path = '/Users/shahafgressel/Documents/צה״ל/הכשרה - git/Shahaf/advanced/advanced 6/costumers'  #updates the json file
            with open(f'{dir_path}/{account_transfer.account_number}.json', 'w') as file:
                account_dir = {'name': account_transfer.name, 'account_number': account_transfer.account_number, 'balance': account_transfer.balance}
                file.write(json.dumps(account_dir))

            conn.sendall(f'You have transfer {to_transfer} ILS to account number {account.account_number}'.encode('utf-8'))


        if not is_exist or not sender_is_exist:
            conn.sendall('No such account!'.encode('utf-8'))

def main():
    bank = Bank()

    bank.start_listen()

if __name__ == "__main__":
        main()