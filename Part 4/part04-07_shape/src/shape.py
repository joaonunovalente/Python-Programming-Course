# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
# Copy here code of line function from previous exercise
def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def triangle(size, character):
    # You should call function line here with proper parameters
    count = 1
    while count <= size:
        line(count, character)
        count += 1

def square(width, height, character):
    # You should call function line here with proper parameters
    count = 1
    while count <= height:
        line(width, character)
        count += 1

def shape(size1, character1, size2, character2):
    triangle(size1, character1)
    square(size1, size2, character2)



# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")

