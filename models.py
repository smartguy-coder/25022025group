import uuid


class Person:
    def __init__(self, name: str):
        self.name: str = name
        self.inn: uuid.UUID = uuid.uuid4()

    def __str__(self):
        return f'<Person {self.name} - {self.inn}>'


class BankAccount:
    def __init__(self, client: Person):
        self.client = client
        self.balance = 0

    def deposit(self, amount):
        self.balance +=


class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []
