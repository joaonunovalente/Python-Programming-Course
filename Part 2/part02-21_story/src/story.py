# Write your solution here

words = ""
last_word = ""
while True:
    word = input("Please type in a word:")
    if word == last_word or word == "end":
        break
        
    last_word = word

    words += word + " "

print(words)
