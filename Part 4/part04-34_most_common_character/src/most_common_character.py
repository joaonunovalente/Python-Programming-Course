# Write your solution here

def most_common_character(my_string: str) -> str:
    most_common = 0
    char = ""
    for character in my_string:
        if my_string.count(character) > most_common:
            most_common = my_string.count(character)
            char = character

    return char


if __name__ == "__main__":
    my_string = "abcdbde"
    most_common_character(my_string)