# Write your solution here
list = []

option = ""
while True:
    print("The list is now", list)
    option = input("a(d)d, (r)emove or e(x)it: ")
    if option == "d":
        list.append(len(list) + 1)
    elif option == "r":
        list.remove(list[-1])
    elif option == "x":
        break

print("Bye!")