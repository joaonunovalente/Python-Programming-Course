class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    
class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.suitcase_items: list = []
        self.suitcase_weight = 0
    
    def add_item(self, item: "Item"):
        if self.suitcase_weight + item.weight() <= self.max_weight:
            self.suitcase_items.append(item)
            self.suitcase_weight += item.weight()

    def number_items(self):
        return len(self.suitcase_items)
    
    def print_items(self):
        for item in self.suitcase_items:
            print(item)

    def weight(self):
        return self.suitcase_weight
    
    def heaviest_item(self):
        heaviest_item = Item("", 0)
        for item in self.suitcase_items:
            if heaviest_item.weight() < item.weight():
                heaviest_item = item
        return heaviest_item
    
    def __str__(self):
        if self.number_items() == 1:
            return f"{self.number_items()} item ({self.suitcase_weight} kg)"
        return f"{self.number_items()} items ({self.suitcase_weight} kg)"
    
class CargoHold:
    def __init__(self, max_weight: int):
        self.max_weight: int = max_weight
        self.suitcase_list: list = []
        self.cargo_weight = 0

    def add_suitcase(self, suitcase: "Suitcase"):
        if self.cargo_weight + suitcase.weight() <= self.max_weight:
            self.suitcase_list.append(suitcase)
            self.cargo_weight += suitcase.weight()

    def number_suitcases(self):
        return len(self.suitcase_list)
    
    def print_items(self):
        for suitcase in self.suitcase_list:
            suitcase.print_items()

    def __str__(self):
        if self.number_suitcases() == 1:
            return f"{self.number_suitcases()} suitcase, space for {self.max_weight - self.cargo_weight} kg"
        return f"{self.number_suitcases()} suitcases, space for {self.max_weight - self.cargo_weight} kg"

if __name__ == "__main__":
    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    suitcase.weight()
