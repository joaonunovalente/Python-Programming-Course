# Write your solution here

number = int(input("Please type in a number:"))
count1 = 1
while count1 <= number:
    count2 = 1

    while count2 <= number:
        print(f"{count1} x {count2} = {count1 * count2}")
        count2 += 1
    
    count1 += 1