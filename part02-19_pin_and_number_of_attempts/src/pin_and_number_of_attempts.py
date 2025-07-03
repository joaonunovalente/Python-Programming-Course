# Write your solution here
attempts = 1
while True:
    pin = int(input("PIN:"))

    if pin == 4321:
        break
    else:
        attempts += 1
        print("Wrong")

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")

