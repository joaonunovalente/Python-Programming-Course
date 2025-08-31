def read_data(filename: str) -> list:
    data = []

    with open(filename) as file:
        for line in file:
            line = line.strip()
            parts = line.split(";")
            temp_list = []
            for part in parts:
                temp_list.append(part)
            
            data.append(temp_list)

    new_data = []
    for operation in data:
        temp_list = []

        temp_list.append(operation[0])
        if len(operation[1].split("+")) > 1:
            parts = operation[1].split("+")
            parts.insert(1, "+")
        elif len(operation[1].split("-")) > 1:
            parts = operation[1].split("-")
            parts.insert(1, "-")

        temp_list.append(parts)
        temp_list.append(operation[2])
        new_data.append(temp_list)

    data = new_data[:]

    return data


def filter_solutions():
    filename = "solutions.csv"
    data = read_data(filename)

    filename_correct = "correct.csv"
    filename_incorrect = "incorrect.csv"
    with open(filename_correct, "w") as file:
        pass
    with open(filename_incorrect, "w") as file:
        pass

    with open(filename_correct, "a") as file_correct:
        for operation in data:
            result1 = int(operation[1][0]) + int(operation[1][2])
            result2 = int(operation[1][0]) - int(operation[1][2])

            if result1 == int(operation[2]) or result2 == int(operation[2]):  
                line = f"{operation[0]};{operation[1][0]}{operation[1][1]}{operation[1][2]};{operation[2]}"
                file_correct.write(line+"\n")


    with open(filename_incorrect, "a") as file_incorrect:
        for operation in data:
            result1 = int(operation[1][0]) + int(operation[1][2])
            result2 = int(operation[1][0]) - int(operation[1][2])

            if result1 != int(operation[2]) and result2 != int(operation[2]):  
                line = f"{operation[0]};{operation[1][0]}{operation[1][1]}{operation[1][2]};{operation[2]}"
                file_incorrect.write(line+"\n")
    


if __name__ == "__main__":
    filter_solutions()