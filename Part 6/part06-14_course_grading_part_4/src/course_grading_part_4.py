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

def read_data_course_information(filename: str) -> dict:
    """Returns the list with the course information."""
    course_information: dict = {}
    with open(filename) as file:
        for line in file:
            parts = line.split(":")
            course_information[parts[0]] = parts[1].strip()

    return course_information


def write_data_statistics(student_dictionary, 
             exercise_dictionary, 
             exam_points_dictionary, 
             course_information):
    """Writes into a .txt file the statistics."""

    with open("results.txt", "w") as file:       
        #----------------------------------
        # Writes title
        #----------------------------------
        name = course_information["name"]
        course = course_information["study credits"]
        title = f"{name}, {course} credits"

        file.write(title + "\n")
        file.write("=" * len(title) + "\n")

        #----------------------------------
        # Writes header line
        #----------------------------------
        message_header = f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}"
        file.write(message_header + "\n")
        
        #----------------------------------
        # Writes table data
        #----------------------------------
        for id, values in student_dictionary.items():
            name = values[0]
            course = values[1]
            name_and_course = name + " " + course

            execise_points_list = exercise_dictionary[id]
            exam_points_list = exam_points_dictionary[id]
            results = find_grade(execise_points_list, exam_points_list)
            
            message_body = f"{name_and_course:30}{results[0]:<10}{results[1]:<10}{results[2]:<10}{results[3]:<10}{results[4]:<10}"
            file.write(message_body + "\n")

    return


def write_data_results(student_dictionary, 
             exercise_dictionary, 
             exam_points_dictionary):

    with open("results.csv", "w") as file:
        for id, values in student_dictionary.items():
            name = values[0]
            course = values[1]

            execise_points_list = exercise_dictionary[id]
            exam_points_list = exam_points_dictionary[id]
            results = find_grade(execise_points_list, exam_points_list)
            grade = results[4]

            # Write into .csv file
            line = f"{id};{name} {course};{grade}\n"
            file.write(line)
            
    return


def main():
    if True:
        # this is never executed
        student_info_filename = input("Student information: ")
        exercise_data_filename = input("Exercises completed: ")
        points_data_file_filename = input("Exam points: ")
        course_information_filename = input("Course information: ")
    else:
        # hard-coded input
        student_info_filename = "students1.csv"
        exercise_data_filename = "exercises1.csv"
        points_data_file_filename = "exam_points1.csv"
        course_information_filename = "course1.txt"

    student_dictionary = read_data_from_file(student_info_filename)
    exercise_dictionary= read_data_from_file(exercise_data_filename)
    exam_points_dictionary = read_data_from_file(points_data_file_filename)
    course_information = read_data_course_information(course_information_filename)

    write_data_statistics(student_dictionary, 
             exercise_dictionary, 
             exam_points_dictionary, 
             course_information)
    write_data_results(student_dictionary, 
             exercise_dictionary, 
             exam_points_dictionary)

main()

