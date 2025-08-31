def search(persons):
    name = input("name: ")
    if name in persons:
        for phone_number in persons[name]:
            print(phone_number)
    else:
        print("no number")
 
def add(persons):
    name = input("name: ")
    number = input("number: ")
    if name not in persons:
        persons[name] = [number]
    elif name in persons:
        persons[name].append(number)
    print("ok!")
 
def main():
    persons = {}
    while True:
        cmd = input("command (1 search, 2 add, 3 quit): ")
        if cmd == "1":
            search(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            break
    print("quitting...")
 
main()