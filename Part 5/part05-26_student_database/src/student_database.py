# Write your solution here

def add_student(students: dict, name: str):
    students[name] = []
    return


def print_student(students, name):
    if name in students:
        number_of_courses = len(students[name])
        value = students[name]
        print(f"{name}:")
        if number_of_courses > 0:
            average = compute_average(value)
            message = f" {number_of_courses} completed courses:"
            print(message)
            for i in range(0,len(students[name])):
                print(" ", value[i][0], value[i][1])
            print(f" average grade {average:.1f}")
        else: 
            print(" no completed courses")
    else:
        print(f"{name}: no such person in the database")
    return 


def add_course(students: dict, name: str, couse_and_grade: tuple[str, int]):
    # Define variables: course and grade
    course = couse_and_grade[0]
    grade = couse_and_grade[1]

    # Don't add the course if grade = 0
    if grade == 0:
        return
    
    if name not in students:
        return
    
    # Checking if the course already exists in the database associated with the student
    values = students[name]

    for item in values:
        if course == item[0] and grade < item[1]:
            return
        elif course == item[0] and grade > item[1]:
            students[name].remove(item)

    # Adding the course
    students[name].append(couse_and_grade)


def compute_average(value: list):
    grade_list = []
    for item in value:
        grade_list.append(item[1])
    average = sum(grade_list) / len(value)
    return average


def summary(students: dict):
    number_of_students = len(students)

    max_courses = 0
    max_average = 0
    for key, value in students.items():
        # Maximum number of courses
        if len(value) > max_courses:
            max_courses = len(value)
            name_course = key
        # Best average grade
        average = compute_average(value)
        if average > max_average:
            max_average = average
            name_average = key
    # --------------------------------
    # Priting
    # --------------------------------
    print("students", number_of_students)
    print("most courses completed", max_courses, name_course)
    print("best average grade", max_average, name_average)

    return


if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
    summary(students)
