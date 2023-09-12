import socket

def main():
    HOST = '127.0.0.1'
    PORT = 234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(HOST, PORT)
    server_socket.listen()

    print(f'listening on {HOST} on port {PORT}')

    while True:
        conn, addr = server_socket.accept()
        print(f'connected to {addr}')

        data = conn.recv(1024)
        if data:
            print(str(data))
            conn.sendall('received')

        elif data == b'stop':
            break

    server_socket.close()


if __name__ == "__main__":
    main()