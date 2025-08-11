# Write your solution here
# You can test your function by calling it within the following block

def greatest_number(x, y, z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z

if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)