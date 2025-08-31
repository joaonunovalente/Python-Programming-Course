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


def find_grade(exercise_points: list, exam_points: list) -> list:
    exercise_number = int(sum(map(int, exercise_points)))
    exercise_points_total = int(sum(map(int, exercise_points)) * 10 / 40)
    exam_points_total = sum(map(int, exam_points))
    points_total = exercise_points_total + exam_points_total

    if points_total < 15:
        grade = 0
    elif 15 <= points_total < 18:
        grade = 1
    elif 18 <= points_total < 21:
        grade = 2
    elif 21 <= points_total < 24:
        grade = 3
    elif 24 <= points_total < 28:
        grade = 4
    else:
        grade = 5
    
    results = [exercise_number, 
               exercise_points_total, 
               exam_points_total, 
               points_total,
               grade]
    
    return results


def printing(student_dictionary, exercise_dictionary, exam_points_dictionary):
    print(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}")
    
    for id, values in student_dictionary.items():
        name = values[0]
        course = values[1]
        name_and_course = name + " " + course

        execise_points_list = exercise_dictionary[id]
        exam_points_list = exam_points_dictionary[id]
        results = find_grade(execise_points_list, exam_points_list)
        
        print(f"{name_and_course:30}{results[0]:<10}{results[1]:<10}{results[2]:<10}{results[3]:<10}{results[4]:<10}")

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

