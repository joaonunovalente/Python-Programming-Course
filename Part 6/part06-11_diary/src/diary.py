filename = "diary.txt"
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    mode = int(input("Function: "))
    

    if mode == 1:
        diary_input = input("Diary input: ")
        with open(filename, "a") as file:
            file.write(diary_input + "\n")
        print("Diary saved")
    elif mode == 2:
        with open(filename) as file:
            print("Entries:")
            for line in file:
                line = line.strip()
                print(line)

    elif mode == 0:
        break
print("Bye now!")
