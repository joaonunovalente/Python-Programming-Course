# Write your solution here

def distinct_numbers(my_list : list):
    new_list = []
    for n in my_list:
        if n not in new_list:
            new_list.append(n)
            
    new_list.sort()
    return new_list


if __name__ == "__main__":
    my_list = [5, 6, 7, 8, 8, 9, 9, 5]
    distinct_numbers(my_list)