import string

# Write your solution here
def run(program: list) -> list:
    output_list: list = []

    # Dictionary with all variables
    aDict = dict.fromkeys(string.ascii_uppercase, 0)
    print(aDict)


    return output_list

if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)
