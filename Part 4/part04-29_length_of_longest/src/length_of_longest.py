# Write your solution here

def length_of_longest(my_list : list):
    longest = ""
    for word in my_list:
        if len(word) > len(longest):
            longest = word
            print(longest)
    lenght = len(longest)

    return lenght


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    length_of_longest(my_list)