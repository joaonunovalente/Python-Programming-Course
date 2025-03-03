def filter_incorrect():

    lottery_dictionary = {}
    with open("lottery_numbers.csv") as file:
        for line in file:
            line = line.strip()
            parts = line.split(";")
            week = parts[0]
            print
            temp_list = []
            if week.split(" ")[1].isdigit():            
                numbers = parts[1].split(",")
                if len(numbers) == 7:
                    for number in numbers:
                        
                        if number.isdigit() == False or 0 <= int(number) > 40 or number in temp_list:
                            break
                        else:
                            temp_list.append(number)

            if len(temp_list) == 7:
                lottery_dictionary[week.split(" ")[1]] = temp_list


    with open("correct_numbers.csv", "w") as file:
        started = "yes"
        for key, value in lottery_dictionary.items():
            line = f"week {key};{value[0]},{value[1]},{value[2]},{value[3]},{value[4]},{value[5]},{value[6]}"
            if started == "no":
                file.write(line)
                started = "no"
            else:
                file.write("\n" + line)

    return


if __name__ == "__main__":
    filter_incorrect()