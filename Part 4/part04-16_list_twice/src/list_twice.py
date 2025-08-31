# Write your solution here

list = []
list_sorted = []

while True:
    item = int(input("New item: "))
    if item == 0:
        break
    list.append(item)
    list_sorted = sorted(list)

    print("The list now:", list)
    print("The list in order:", list_sorted)

print("Bye!")