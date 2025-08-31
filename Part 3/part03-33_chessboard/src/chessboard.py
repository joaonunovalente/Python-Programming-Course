# Write your solution here

def chessboard(size):
    count1 = 1
    while count1 <= size:
        count2 = 1
        string = ""
        while count2 <= size: 
            if count1 % 2 == 1:      
                if count2 % 2 == 1:
                    string += "1"
                else:
                    string += "0"
                count2 += 1
            else:
                if count2 % 2 == 1:
                    string += "0"
                else:
                    string += "1"
                count2 += 1

        print(string)

        count1 += 1
                



# Testing the function
if __name__ == "__main__":
    chessboard(3)
