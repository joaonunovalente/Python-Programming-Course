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

def printing(student_dictionary, exercise_dictionary):

    for id, values in student_dictionary.items():
        name = values[0]
        course = values[1]
        if id in exercise_dictionary:
            number_exercises = sum(map(int, exercise_dictionary[id]))
            print(name, course, number_exercises)

    return

def main():
    if True:
        # this is never executed
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
    else:
        # hard-coded input
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"

    student_dictionary = read_data_from_file(student_info)
    exercise_dictionary= read_data_from_file(exercise_data)
    printing(student_dictionary, exercise_dictionary)

main()

