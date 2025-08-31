from fractions import Fraction


def fractionate(amount: int):
    fraction_list = []
    for i in range(0, amount):
        fraction_list.append(Fraction(1, amount))        

    return fraction_list

if __name__ == "__main__":
    fractionate(3)