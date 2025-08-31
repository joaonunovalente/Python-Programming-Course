import string
import operator

# Write your solution here
def run(program: list) -> list:
    output_list: list = []

    # Dictionary with all charaters set to 0
    characters: dict = dict.fromkeys(string.ascii_uppercase, 0)
    # List with all commads
    commands: list = ['PRINT', 'MOV', 'ADD', 'SUB', 'MUL', 'END']
    # Dictionary of variables
    line_variables: dict = {}
    # Dictionary of operators
    ops: dict= {
        '==': operator.eq,
        '!=': operator.ne,
        '>' : operator.gt,
        '>=': operator.ge,
        '<' : operator.lt,
        '<=': operator.le,
    }

    # Extract the line varibles first
    i = 0
    for program_line in program:
        part: list = program_line.split()
        if part[0][-1] == ":":
            line_variables[part[0][:-1]] = i
        i += 1        

    i = 0
    while i < len(program):
        program_line = program[i]
        part = program_line.split()
        command = part[0] 
        print(part)
        if len(part) == 2 and part[0] == 'PRINT':
            if part[1].isnumeric():
                pass
            else:
                part[1] = characters[part[1]]            

        if len(part) == 3:
            if part[2].isnumeric():
                pass
            else:
                part[2] = characters[part[2]]
            
        if len(part) == 6:
            if part[3].isnumeric():
                pass
            else:
                part[3] = characters[part[3]]

        
        if command == 'MOV':
            characters[part[1]] = int(part[2])
        elif command == 'ADD':
            characters[part[1]] = int(characters[part[1]]) + int(part[2])
        elif command == 'SUB':
            characters[part[1]] = int(characters[part[1]]) - int(part[2])
        elif command == 'MUL':
            characters[part[1]] = int(characters[part[1]]) * int(part[2])
        elif command == 'PRINT':
            output_list.append(int(part[1]))
        elif command == 'IF':
            if part[2] == '==':
                if characters[part[1]] == int(part[3]):
                    i = line_variables[part[5]]
            if part[2] == '!=':
                if characters[part[1]] != int(part[3]):
                    i = line_variables[part[5]]
            if part[2] == '>':
                if characters[part[1]] > int(part[3]):
                    i = line_variables[part[5]]    
            if part[2] == '>=':
                if characters[part[1]] >= int(part[3]):
                    i = line_variables[part[5]]  
            if part[2] == '<':
                if characters[part[1]] < int(part[3]):
                    i = line_variables[part[5]]    
            if part[2] == '<=':
                if characters[part[1]] <= int(part[3]):
                    i = line_variables[part[5]]                                                                    

        elif command == 'END':
            break
        elif command == 'JUMP':
            i = line_variables[part[1]]

        print(characters)
        
        i += 1


    return output_list

if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)
