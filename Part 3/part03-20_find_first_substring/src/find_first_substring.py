# Write your solution here

word = input("Please type in a word:")
char = input("Please type in a character:")

index = word.find(char)
if len(word) - index > 2:
    print(word[index:index+3])
    