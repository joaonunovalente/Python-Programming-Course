# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")

# Auxiliar variables
count = 0
addition = 0
positive = 0
negative = 0

while True:
    number = int(input("Number:"))

    addition += number
    
    # Check for positive numbers
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    

    if number == 0:
        mean = addition / count
        break
    
    count += 1

print("... the program asks for numbers")
print("Numbers typed in", count)
print("The sum of the numbers is", addition)
print("The mean of the numbers is", mean)
print("Positive numbers", positive)
print("Negative numbers", negative)

