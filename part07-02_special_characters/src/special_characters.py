from string import (
    ascii_letters, 
    punctuation
    )


def separate_characters(my_string: str):
    letters = ""
    punctuations = ""
    others = ""

    for character in my_string:
        if character in ascii_letters:
            letters += character
        elif character in punctuation:
            punctuations += character
        else:
            others += character
    
    return letters, punctuations, others


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])