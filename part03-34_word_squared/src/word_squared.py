# Write your solution here

def squared(string, size):
    count = 1
    row = string * size ** 2
    while count <= size:
        
        print(row[:size])
        row = row[size:]
        count += 1
        

    

    


if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)