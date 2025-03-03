# Write your solution here
# You can test your function by calling it within the following block
def first_word(sentence):
    index = sentence.find(" ")
    return sentence[:index]


def second_word(sentence):
    index = sentence.find(" ")
    sentence = sentence[index + 1:]

    if  sentence.find(" ") == -1:
        return sentence
        
    index = sentence.find(" ")

    return sentence[:index]


def last_word(sentence):
    index = 1
    while index != -1:
        index = sentence.find(" ")
        sentence = sentence[index + 1:]
    return sentence    


if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word("first second"))
    print(last_word(sentence))