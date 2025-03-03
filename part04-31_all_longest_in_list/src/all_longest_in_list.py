def all_the_longest(my_list : list) -> list:

    new_list = []
    longest = ""
    for word in my_list:
        if len(word) > len(longest):
            new_list.clear()
            new_list.append(word)
            longest = word
        elif len(word) == len(longest):
            new_list.append(word)
            longest = word
        



        
    print(new_list)
    return new_list


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    all_the_longest(my_list)