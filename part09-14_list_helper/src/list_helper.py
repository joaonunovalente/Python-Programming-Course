from itertools import groupby

class ListHelper:
    def __init__(self):
        pass

    @classmethod
    def greatest_frequency(cls, my_list: list):
        output = [len(list(group)) for key, group in groupby(sorted(my_list))]
        unique_list = list(dict.fromkeys(my_list))
        return unique_list[output.index(max(output))]
    
    @classmethod
    def doubles(cls, my_list:list):
        output = [len(list(group)) for key, group in groupby(sorted(my_list))]
        transformed = [1 if x > 1 else 0 for x in output]
        return sum(transformed)

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))