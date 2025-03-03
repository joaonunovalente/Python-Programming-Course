# Write your solution here

def list_of_stars(my_list : list):
    for n in my_list:
        print("*" * n)


if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])