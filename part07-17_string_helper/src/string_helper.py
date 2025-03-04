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


if __name__ == "__main__":
    #Test functions
    print(change_case("Well hello there!"))