# Copy here code of line function from previous exercise
def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    count = 1
    while count <= size:
        line(size, "#")
        count += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
