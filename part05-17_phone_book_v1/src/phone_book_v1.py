phone_book = {}
while True:
    option = int(input("command (1 search, 2 add, 3 quit): "))

    if option == 1:
        name = input("name: ")
        if name in phone_book:
            print(phone_book[name])
        else:
            print("no number")
    elif option == 2:
        name = input("name: ")
        number = input("number: ")
        phone_book[name] = number
        print("ok!")
    elif option == 3:
        print("quitting...")
        break



