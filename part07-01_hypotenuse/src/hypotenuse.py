from math import sqrt


def hypotenuse(leg1:float, leg2: float) -> float:
    result = sqrt(leg1 ** 2 + leg2 ** 2)
    return result


if __name__ == "__main__":
    print(hypotenuse(3,4))