# Write your solution here

word = input("Word:")

print("*" * 30)
string1 = "*"
if len(word) % 2 == 0:
    string2 = " " * int(14 - (len(word) / 2) ) + word +  " " * int(14 - (len(word) / 2))
else:
    string2 = " " * int(14 - (len(word) / 2) ) + word +  " " * int(15 - (len(word) / 2))
string3 = "*"
string = string1 + string2 + string3
print(string)
print("*" * 30)