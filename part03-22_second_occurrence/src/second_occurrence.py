# Write your solution here

string = input("Please type in a string:")
substring = input("Please type in a substring:")

length = len(string)
index1 = string.find(substring)

string = string[index1 + len(substring):]


index2 = string.find(substring)

if index2 == -1:
    print("The substring does not occur twice in the string.")
else: 
    occurrence = len(substring) + index1 + index2
    print("The second occurrence of the substring is at index " + str(occurrence) + ".")