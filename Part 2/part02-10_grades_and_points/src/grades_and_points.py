# Write your solution here
points = int(input("How many points [0-100]:"))

if points < 0:
    print("Grade: impossible!")
elif 0 <= points < 50:
    print("Grade: fail")
elif 50 <= points < 60:
    print("Grade: 1")
elif 60 <= points < 70:
    print("Grade: 2")
elif 70 <= points < 80:
    print("Grade: 3")
elif 80 <= points < 90:
    print("Grade: 4")
elif 90 <= points <= 100:
    print("Grade: 5")
else:
    print("Grade: impossible!")