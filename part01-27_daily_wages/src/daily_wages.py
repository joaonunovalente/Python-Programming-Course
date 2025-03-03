# Write your solution here
hourly_wage = float(input("Hourly wage:"))
hours_worked = float(input("Hours worked:"))
day = input("Day of the week:")

if day != "Sunday":
    print("Daily wages:", hourly_wage * hours_worked, "euros")
else:
    print("Daily wages:", hourly_wage * hours_worked * 2, "euros")