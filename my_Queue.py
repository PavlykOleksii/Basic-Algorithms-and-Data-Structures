from queue import Queue
import random

class Client:
    def __init__(self, name):
        self.name = name
        self.operation = random.randint(1, 9)  # Random number of operations between 1 and 5

class Bank:
    def __init__(self):
        self.clients = Queue()

    def new_client(self, client):
        self.clients.put(client)

    def serve_clients(self):
        while not self.clients.empty():
            current_client = self.clients.get()
            print(f"Обслуговуємо клієнта {current_client.name} з {current_client.operation} операціями.")

bank = Bank()

for i in range(10):
    bank.new_client(Client(f"Клієнт {i+1}"))

bank.serve_clients()