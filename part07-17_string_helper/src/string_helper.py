# Write your solution here

def change_case(orig_string: str) -> str:
    torned_string: str = ""
    
    for letter in orig_string:
        if letter.islower():
            torned_string += letter.upper()
        elif letter.isupper():
            torned_string += letter.lower()
        else:
            torned_string += letter
    
    return torned_string

def split_in_half(orig_string: str) -> tuple:
    half = int(len(orig_string) / 2) # equals 8

    p1 = orig_string[0:half]
    p2 = orig_string[half:]
    
    return (p1, p2)

def remove_special_characters(orig_string: str):
    no_characters: str = ""

    for letter in orig_string:
        if letter.isalnum() or letter ==" ":
            no_characters += letter
            
    return no_characters


if __name__ == "__main__":
    #Test functions
    string = "Well hello there!"
    print(change_case(string))
    print(split_in_half(string))
    print(remove_special_characters("This is a test, lets see how it goes!!!11!"))