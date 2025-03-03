import copy

if True:
    text = input("Write text: ")
else:
    text = "We use ptython to make a spell checker"

text_words = text.split(" ")
# print(text_words)

with open("wordlist.txt") as file:
    dictionary = []
    for line in file:
        line = line.replace("\n", "")
        line.lower()
        dictionary.append(line)
message = ""
for word in text_words:
    new_word = copy.deepcopy(word)
    
    if new_word.lower() not in dictionary:
        message = message + " *" + word + "*"
    else:
        message = message + " " + word
print(message)
    

