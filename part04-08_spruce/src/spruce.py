# Write your solution here

def tree_log(size):
    print(" " * int((size * 2 - 2) / 2) + "*")

def tree(size):
    count = 1
    count2 = size * 2 - 2
    count3 = 1
    while count <= size:
        print(" " * int(count2 / 2) + "*" * count3)
        count += 1
        count2 -= 2
        count3 += 2

def spruce(size):
    print("a spruce!")
    tree(size)
    tree_log(size)

if __name__ == "__main__":
    spruce(3)