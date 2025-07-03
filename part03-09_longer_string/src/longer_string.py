# Write your solution here
word1 = input("Please type in a string 1:")
word2 = input("Please type in a string 2:")
if len(word1) > len(word2):
    output = f"{word1} is longer"
elif len(word1) < len(word2):
    output = f"{word2} is longer"
else:
    output = "The strings are equally long"

print(output)