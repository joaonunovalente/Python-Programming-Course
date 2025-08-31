from random import sample


def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    possible_numbers = [*range(lower,upper)]
    numbers_drawn = sample(possible_numbers, amount)
    numbers_drawn.sort()

    print(numbers_drawn)

    return numbers_drawn

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)