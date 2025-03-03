# Write your solution here
def read_input(text: str, min_number: int, max_number: min) -> int:

    while True:
        try:
            number = int(input(text))
            if min_number <= number <= max_number:
                return number
        except ValueError:
            pass
        
        print(f"You must type in an integer between {min_number} and {max_number}")






if __name__ == "__main__":
    
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)