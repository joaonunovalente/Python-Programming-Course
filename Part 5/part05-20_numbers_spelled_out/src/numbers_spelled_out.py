# Write your solution here
def dict_of_numbers() -> dict:
    numbers = {}
    # Possible combinations
    numbers[0] = "zero"
    numbers[1] = "one"
    numbers[2] = "two"
    numbers[3] = "three"
    numbers[4] = "four"
    numbers[5] = "five"
    numbers[6] = "six"
    numbers[7] = "seven"
    numbers[8] = "eight"
    numbers[9] = "nine"
    numbers[10] = "ten"
    numbers[11] = "eleven"
    numbers[12] = "twelve"
    numbers[13] = "thirteen"
    numbers[14] = "fourteen"
    numbers[15] = "fifteen"
    numbers[16] = "sixteen"
    numbers[17] = "seventeen"
    numbers[18] = "eighteen"
    numbers[19] = "nineteen"

    numbers[20] = "twenty"
    numbers[30] = "thirty"
    numbers[40] = "forty"
    numbers[50] = "fifty"
    numbers[60] = "sixty"
    numbers[70] = "seventy"
    numbers[80] = "eighty"
    numbers[90] = "ninety"

    for number in range(20, 100):
        remainder = number % 10
        division = int(number / 10) * 10
        if remainder != 0:
            number_sppeled = numbers[division] +"-" + numbers[remainder]
            numbers[number] = number_sppeled


    return numbers


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers)
    # print(numbers[11])
    # print(numbers[45])
    # print(numbers[99])
    # print(numbers[0])