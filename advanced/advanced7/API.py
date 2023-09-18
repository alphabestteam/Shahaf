import socket

def connect_new_account() -> None:
    HOST = '127.0.0.1'
    PORT = 12346

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    new_account()

def connect_transfer() -> None:
    HOST = '127.0.0.1'
    PORT = 12346

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    transfer()

def new_account() -> None:
    HOST = '127.0.0.1'
    PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    client_socket.sendall('1'.encode('utf-8'))

    name = input('Enter the name of client: ')
    client_socket.sendall(name.encode('utf-8'))
    
    balance = input('Please enter the start balance of client: ')
    client_socket.sendall(balance.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    print(data)

    client_socket.close()

def deposit_or_withdraw() -> None:
    HOST = '127.0.0.1'
    PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    client_socket.sendall('2'.encode('utf-8'))

    answer = input('To deposit enter 1 \nTo withdraw enter 2\n')
    client_socket.sendall(answer.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    name = input()
    client_socket.sendall(name.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    account_number = input()
    client_socket.sendall(account_number.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    money = input()
    client_socket.sendall(money.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    
    client_socket.close()

def transfer(register_account) -> None:
    HOST = '127.0.0.1'
    PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    client_socket.sendall('3'.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    sender_name = input()
    client_socket.sendall(sender_name.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    sender_account_number = input()
    client_socket.sendall(sender_account_number.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    money = input()
    client_socket.sendall(money.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    name = input()
    client_socket.sendall(name.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    
    if account_number != None:
        account_number = register_account

    else:
        account_number = input()

    client_socket.sendall(account_number.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    
    client_socket.close()

# def main():

#     new_account()

#     deposit_or_withdraw()

#     transfer()


# if __name__ == "__main__":
#     main()