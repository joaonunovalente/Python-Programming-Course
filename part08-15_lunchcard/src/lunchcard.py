class LunchCard():
    def __init__(self,  balance: float):
        self.balance: float = balance

    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60
    
    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60

    def deposit_money(self, money_added: int):
        if money_added <= 0:
            raise ValueError
        else:
            self.balance += money_added

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print("Peter: " + f"The balance is {peters_card.balance:.1f} euros")
print("Grace: " + f"The balance is {graces_card.balance:.1f} euros")

peters_card.deposit_money(20)
graces_card.eat_special()
print("Peter: " + f"The balance is {peters_card.balance:.1f} euros")
print("Grace: " + f"The balance is {graces_card.balance:.1f} euros")

peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print("Peter: " + f"The balance is {peters_card.balance:.1f} euros")
print("Grace: " + f"The balance is {graces_card.balance:.1f} euros")
