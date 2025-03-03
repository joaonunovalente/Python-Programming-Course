# Write your solution here

def same_chars(string, x, y):
    if 0 < x > len(string) - 1 or 0 < y > len(string)- 1:
        return False

    if string[x] == string[y]:
        return True
    else:
        return False



# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))