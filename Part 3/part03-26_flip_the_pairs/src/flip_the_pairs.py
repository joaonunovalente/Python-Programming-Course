# Write your solution here
number = int(input("Please type in a number:"))

count1 = 2
count2 = -1
while count1 <= number:
    while count2 < 0:
        print(count1)
        print(count1 + count2)
        count2 += 1
    count2 = -1    
    count1 += 2
    
if number % 2 == 1:
    print(number)