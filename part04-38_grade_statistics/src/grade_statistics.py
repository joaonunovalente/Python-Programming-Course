def ask_results() -> tuple[list, list]:
    points = []
    exercises = []

    while True:
        answer = input("Exam points and exercises completed: ")
        if answer == "":
            break
        space_index = answer.find(" ")
        points.append(answer[:space_index])
        exercises.append(answer[space_index + 1:])

    return points, exercises


def statistics(exercises: list, points: list) -> tuple[list, float, float]:
    # -------------------------
    #       Compute grade
    # -------------------------
    grade = []

    for index in range(0,len(exercises)):
        exercises[index] = int(int(exercises[index]) / 10)
        points[index] = int(points[index])
        final_result = points[index] + exercises[index]

        if 0 <= final_result <= 14 or points[index] < 10:
            grade.append(0)
        elif final_result <= 17:
            grade.append(1)
        elif final_result <= 20:
            grade.append(2)
        elif final_result <= 23:
            grade.append(3)
        elif final_result <= 27:
            grade.append(4)
        elif final_result <= 30:
            grade.append(5)

    # ---------------------------------------------------------------
    #       Compute average and success rate (percentage)
    # ---------------------------------------------------------------
    average = (sum(points)  + sum(exercises)) / len(points)
    percentage = (( len(grade) - grade.count(0)) / len(grade)) * 100 

    return grade, average, percentage


def grade_distribuition(grade: list) -> list:
    distribution = []
    for n in range(0,6):       
        distribution.append(grade.count(n))

    return distribution


def printing( average, percentage, distribution):
    print("Statistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {percentage:.1f}")
    print("Grade distribution: ")
    for n in range(5,-1,-1):
        print(f"  {n}: {"*" * distribution[n]}")
    

def main():
    exercises, points = ask_results()
    grade, average, percentage = statistics(points, exercises)
    distribution = grade_distribuition(grade)
    printing(average, percentage, distribution)

# -------------------------
#       Run program
# -------------------------
main()


