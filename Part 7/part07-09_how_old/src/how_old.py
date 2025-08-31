from datetime import datetime


# Input arguments
day = int(input("Day: "))
mouth = int(input("Mouth: "))
year = int(input("Year: "))

time_millenium = datetime(2000, 1, 1)
time_user = datetime(year, mouth, day)

difference = time_millenium - time_user
if difference.days > 0:
    print(f"You were {difference.days - 1} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
