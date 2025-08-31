# Write your solution here

def no_vowels(my_string: str) -> str:

    vowels = "aeiou"

    for vowel in vowels:
        # String are immutable !!!!!!
        my_string = my_string.replace(vowel, "")

    return my_string

if __name__ == "__main__":
    my_string = "this is an example"
    no_vowels(my_string)