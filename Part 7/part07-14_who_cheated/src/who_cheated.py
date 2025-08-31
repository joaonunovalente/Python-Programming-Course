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


if __name__ == "__main__":
    cheaters()