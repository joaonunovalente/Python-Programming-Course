# Write your solution here

sentence = input("Please type in a sentence:")
print(sentence[0])

while sentence.find(" ") != -1:
    index = sentence.find(" ")
    sentence = sentence[index + 1:]
    print(sentence[0])
