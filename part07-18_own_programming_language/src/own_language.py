import string

# Write your solution here
def run(program: list) -> list:
    output_list: list = []

    # Dictionary with all variables set to 0
    aDict = dict.fromkeys(string.ascii_uppercase, 0)
    # List with all commads
    commands = ['PRINT', 'MOV', 'ADD', 'SUB', 'MUL', 'END']
    # Dictionary of variables
    line_variables: dict = {}

    # Extract the line varibles first
    i = 0
    for program_line in program:
        part = program_line.split()
        if part[0][-1] == ":":
            line_variables[part[0][:-1]] = i
        i += 1        

    i = 0
    while i < len(program):
        program_line = program[i]
        part = program_line.split()
        command = part[0] 
        print(i)
        print(part)
        print(command)



        if len(part) == 3:
            if part[2].isnumeric():
                pass
            else:
                part[2] = aDict[part[2]]
        
        if command == 'MOV':
            aDict[part[1]] = int(part[2])
        elif command == 'ADD':
            aDict[part[1]] = int(aDict[part[1]]) + int(part[2])
        elif command == 'SUB':
            aDict[part[1]] = int(aDict[part[1]]) - int(part[2])
        elif command == 'MUL':
            aDict[part[1]] = int(aDict[part[1]]) * int(part[2])
        elif command == 'PRINT':
            output_list.append(aDict[part[1]])
        elif command == 'IF':
            print("----------------------\n")
            print(part[2])
            match part[2]:
                case "==":
                    if part[1] == part[3]:
                        i = line_variables[part[3]]
                case "!=":
                    if part[1] != part[3]:
                        i = line_variables[part[3]]
                case ">=":
                    print("ola")
                    if part[1] >= part[3]:
                        i = line_variables[part[5]]
                    else:
                        pass 
        
        elif command == 'END':
            break
        elif command == 'JUMP':
            pass
            # i = line_variables[part[1]]
        
        print(aDict)
        
        i += 1


    return output_list

if __name__ == "__main__":
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)
