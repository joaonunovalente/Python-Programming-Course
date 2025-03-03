# Write your solution here
items = []

number = int(input("How many items: "))
while number > 0:
    item = int(input("Item: "))
    items.append(item)
    number -= 1

print(items)
