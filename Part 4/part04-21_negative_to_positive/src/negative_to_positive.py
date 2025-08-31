# Write your solution here
number = int(input("Please type in a positive integer: "))

for n in range(-number, number + 1):
    if n == 0:
        continue
    print(n)