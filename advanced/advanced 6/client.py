import socket, json

class Client:
    def __init__(self, path: str) -> None:
        with open (path, 'r') as file:
            content = file.read()
            client_dir = json.loads(content)
            
            self.name = client_dir['name']
            self.account_number = client_dir['account_number']
            self.balance = client_dir['balance']