from random import sample
from string import (
    ascii_lowercase,
    digits    
    )


def generate_strong_password(
        password_length: int, 
        numbers: bool, 
        spectial_character: bool
        ) -> str:
    punctuation = "!?=+-()#"
    possible_characters = ascii_lowercase
    if numbers == True:
        possible_characters += digits
    if spectial_character == True:
        possible_characters += punctuation

    while True:
        password = "".join(sample(possible_characters, password_length))
        cond1 = False
        cond2 = False
        if numbers == True:
            for character in password:
                if character in digits:
                    cond1 = True
        elif numbers == False:
            cond1 = True
        if spectial_character == True:
            for character in password:
                if character in punctuation:
                    cond2 = True
        elif spectial_character == False:
            cond2 = True

        print(cond1, cond2)
        if cond1 == True and cond2 == True:

            return password


if __name__ == "__main__":
    print(generate_strong_password(10, False, False))