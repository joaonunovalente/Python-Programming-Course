# Write your solution here
# You can test your function by calling it within the following block

def line(number, string):
    count = 1
    row = ""
    while count <= number:
        if string == "":
            row += "*"
        else:
            row += str(string[0])
        count += 1
    print(row)    

if __name__ == "__main__":
    line(5, "")