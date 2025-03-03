# Write your solution here
fahr = int(input("Please type in a temperature (F):"))

celsius = (fahr - 32) * (5/9)

if celsius >= 0:
    print(f"{fahr} degrees Fahrenheit equals {celsius} degrees Celsius")
else:
    print(f"{fahr} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")
