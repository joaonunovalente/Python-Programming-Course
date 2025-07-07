class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"
    
    def __eq__(self, another):
        number1 = self.__euros + 0.01 * self.__cents
        number2 = another.__euros + 0.01 * another.__cents
        if number1 == number2:
            return True
        else:
            return False

    def __ne__(self, another):
        number1 = self.__euros + 0.01 * self.__cents
        number2 = another.__euros + 0.01 * another.__cents

        if number1 != number2:
            return True
        else:
            return False
        
    def __gt__(self, another):
        number1 = self.__euros + 0.01 * self.__cents
        number2 = another.__euros + 0.01 * another.__cents

        if number1 > number2:
            return True
        else:
            return False
    
    def __lt__(self, another):
        number1 = self.__euros + 0.01 * self.__cents
        number2 = another.__euros + 0.01 * another.__cents

        if number1 < number2:
            return True
        else:
            return False
    
    def __add__(self, another):

        number1 = self.__euros + 0.01 * self.__cents
        number2 = another.__euros + 0.01 * another.__cents
        result = number1 + number2

        result_euros = int(result)
        result_cents = round((result - result_euros) * 100)

        return Money(result_euros, result_cents)

    def __sub__(self, another):

        number1 = self.__euros + 0.01 * self.__cents
        number2 = another.__euros + 0.01 * another.__cents
        result = number1 - number2
        
        result_euros = int(result)
        result_cents = round((result - result_euros) * 100)

        if result < 0:
            raise ValueError("a negative result is not allowed")
        
        return Money(result_euros, result_cents)
    
if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1