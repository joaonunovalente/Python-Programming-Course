# Write your solution here

number = int(input("Please type in a number:"))

count = 1
count2 = 0
while count <= number /2:

    print(count)
    print(number + count2)
    count += 1
    count2 -= 1

if number % 2 == 1:
    print(int(number / 2) + 1)