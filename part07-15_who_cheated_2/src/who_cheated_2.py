# Write your solution here
import csv
from datetime import datetime, timedelta

def read_data() -> tuple[dict, list]:
    start_times: list = []
    with open("start_times.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            start_times.append(line)

    submissions: list = []
    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            submissions.append(line)

    start_times_dict = {}
    for i in start_times:
        start_times_dict[i[0]] = i[1]
    
    return start_times_dict, submissions


def cheaters():
    start_times_dict, submissions = read_data()

    student_cheated: list = []
    students_names: list = list(start_times_dict.keys())

    for student in students_names:
        datetime_str: str = start_times_dict[student]
        datetime_start = datetime.strptime(datetime_str, '%H:%M')
        for attempt in submissions:
            if student == attempt[0] and student not in student_cheated:
                datetime_end = datetime.strptime(attempt[3], '%H:%M')
                time_difference = datetime_end - datetime_start
                if time_difference > timedelta(hours=3):
                    student_cheated.append(student)
    return student_cheated


def final_points()-> dict:

    start_times_dict, submissions = read_data()
    students_names: list = list(start_times_dict.keys())
    results: dict = dict.fromkeys(students_names, [0, 0, 0, 0, 0, 0, 0, 0])
    valid_submissions: list = []

    for student in start_times_dict:
        datetime_str: str = start_times_dict[student]
        datetime_start = datetime.strptime(datetime_str, '%H:%M')
        for attempt in submissions:
            if student == attempt[0]:
                datetime_end = datetime.strptime(attempt[3], '%H:%M')
                time_difference = datetime_end - datetime_start
                if time_difference < timedelta(hours=3):
                    valid_submissions.append(attempt)
    
    print(valid_submissions)
    for attempt in valid_submissions:
        for task in range(0,1):
            if int(attempt[2]) > int(results[attempt[0]][task]):
                results[attempt[0]][task] = int(attempt[2])
    
    print(results)



    number_points: int = 0
    # for student in start_times_dict:
    #     for attempt in valid_submissions:
    #         for task in range(0,8):
    #             if student == attempt[0] and attempt[1] == str(task):
    #                 if int(attempt[2]) > int(results[student][task]):
    #                     print(attempt)
    #                     results[student][task] = int(attempt[2])
        # results[student] = sum(results[student])

        
    # for item in range(0,8):
    #     print(item)
    
    # print(results)
            



    

    # print(valid_submissions)


    return results

if __name__ == "__main__":
    final_points()