import socket

def main():
    HOST = '127.0.0.1'
    PORT = 23456

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    while True:
        message = input('Enter a message: ')
        client_socket.sendall(bytes(message, 'utf-8'))
        data = client_socket.recv(1024)
        print(str(data))


if __name__ == "__main__":
    main()