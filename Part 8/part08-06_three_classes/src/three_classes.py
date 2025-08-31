# Write your solution here
class Checklist:

    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries

class Customer:

    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:

    def __init__(self, model: str, lenght: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = lenght
        self.max_speed = max_speed
        self.bidirectional = bidirectional

if __name__ == "__main__":

    Checklist('header', [1, 2])
    Customer(1, 3.14, 50)
    Cable('model', 3.14, 120, True)