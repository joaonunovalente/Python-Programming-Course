# Write your solution here

def formatted(my_list : list) -> list:
    new_list = []
    for n in my_list:
        string = f"{n:.2f}"
        new_list.append(string)
    return new_list
    

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    formatted(my_list)
