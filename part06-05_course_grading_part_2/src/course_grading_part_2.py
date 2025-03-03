def read_data_from_file(filename: str) -> dict:
    dictionary = {}

    with open(filename) as file:
        it = iter(file) # Make the variable "file" iterable
        next(it, None)  # Skip first item.
        for line in it:
            line = line.replace("\n", "")
            parts = line.split(";")
            dictionary[parts[0]] = []   # Defines the id as the key
            for part in parts[1:]:
                dictionary[parts[0]].append(part)

    return dictionary


def find_grade(exercise_points: list, exam_points: list) -> int:
    exercise_points_total = int(sum(map(int, exercise_points)) * 10 / 40)
    exam_points_total = sum(map(int, exam_points))
    total = exercise_points_total + exam_points_total

    if total < 15:
        grade = 0
    elif 15 <= total < 18:
        grade = 1
    elif 18 <= total < 21:
        grade = 2
    elif 21 <= total < 24:
        grade = 3
    elif 24 <= total < 28:
        grade = 4
    else:
        grade = 5
    
    return grade


def printing(student_dictionary, exercise_dictionary, exam_points_dictionary):
    for id, values in student_dictionary.items():
        name = values[0]
        course = values[1]
        execise_points_list = exercise_dictionary[id]
        exam_points_list = exam_points_dictionary[id]
        grade = find_grade(execise_points_list, exam_points_list)

        print(name, course, grade)
    return


def main():
    if True:
        # this is never executed
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_points_data = input("Exam points: ")
    else:
        # hard-coded input
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
        exam_points_data = "exam_points1.csv"

    student_dictionary = read_data_from_file(student_info)
    exercise_dictionary= read_data_from_file(exercise_data)
    exam_points_dictionary = read_data_from_file(exam_points_data)
    printing(student_dictionary, exercise_dictionary, exam_points_dictionary)

main()

