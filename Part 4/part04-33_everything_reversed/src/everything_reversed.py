# Write your solution here

def everything_reversed(my_list: list) -> list:
    my_list_reversed = my_list[::-1]
    new_list = []
    for word in my_list_reversed:
        new_list.append(word[::-1])

    return new_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    everything_reversed(my_list)