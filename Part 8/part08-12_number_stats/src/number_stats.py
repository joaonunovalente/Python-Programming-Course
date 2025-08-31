# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers: int = 0
        self.numbers_list: list = []
        self.odd_numbers_list: list = []
        self.even_numbers_list: list = []

    def add_number(self, number:int):
        self.numbers += 1
        self.numbers_list.append(number)
        if number % 2 == 1:
            self.odd_numbers_list.append(number)
        else:
            self.even_numbers_list.append(number)

    def count_numbers(self):
        return self.numbers
    
    def get_sum(self):
        if self.numbers == 0:
            return 0 
        
        return sum(self.numbers_list)
    
    def average(self):
        if self.numbers == 0:
            return 0 
        average = self.get_sum() / len(self.numbers_list) 

        return average 
    
number = NumberStats()
number_input = 0
while number_input != -1:
    number_input = int(input("Please type in integer numbers: "))
    if number_input != -1:
        number.add_number(number_input)
    
print(f"Sum of numbers: {number.get_sum()}")
print(f"Mean of numbers: {number.average()}")
print(f"Sum of even numbers: {sum(number.even_numbers_list)}")
print(f"Sum of odd numbers: {sum(number.odd_numbers_list)}")

