import socket

def new_account():
    HOST = '127.0.0.1'
    PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    client_socket.sendall('1'.encode('utf-8'))

    name = input('Enter the name of client: ')
    client_socket.sendall(name.encode('utf-8'))
    balance = int(input('Please enter the start balance of client: '))
    client_socket.sendall(balance.encode('utf-8'))

    client_socket.close()

def deposit_or_withdraw():
    HOST = '127.0.0.1'
    PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    client_socket.sendall('2'.encode('utf-8'))

    answer = input('To deposit enter 1 \nTo withdraw enter 2')
    client_socket.sendall(answer.encode('utf-8'))

    name = input()
    client_socket.sendall(name.encode('utf-8'))

    account_number = input()
    client_socket.sendall(account_number.encode('utf-8'))

    money = input()
    client_socket.sendall(money.encode('utf-8'))
    
    client_socket.close()

def transfer():
    HOST = '127.0.0.1'
    PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    client_socket.sendall('3'.encode('utf-8'))

    name = input()
    client_socket.sendall(name.encode('utf-8'))

    account_number = input()
    client_socket.sendall(account_number.encode('utf-8'))

    money = input()
    client_socket.sendall(money.encode('utf-8'))
    
    client_socket.close()

def main():

    new_account()

    deposit_or_withdraw()

    transfer()


if __name__ == "__main__":
    main()
