# Write your solution here

def shortest(my_list : list):
    longest = my_list[0]
    for word in my_list:
        if len(word) < len(longest):
            longest = word

        

    return longest


if __name__ == "__main__":
    my_list = ['Alan', 'Steve']
    shortest(my_list)