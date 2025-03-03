# Write your solution here
num_students = int(input("How many students on the course?"))
group_desired = int(input("Desired group sizer?"))
modulo = num_students % group_desired
group_size = (num_students // group_desired) + 1

if modulo == 0:
    print("Number of groups formed:", num_students / group_desired)
else:
    print("Number of groups formed:", group_size)
