from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# def sum_of_all_credits(attempts: list):
#     def sum_credits(sum_of_credits, attempt):
#         return sum_of_credits + attempt.credits
#     return reduce(sum_credits, attempts, 0)

def sum_of_all_credits(courses: list):
    return reduce(lambda sum_of_credits, attempt: sum_of_credits + attempt.credits , courses, 0)

def sum_of_passed_credits(courses: list):
    # courses = filter(lambda item: item.grade > 0, courses)
    return reduce(lambda sum_of_credits, attempt: sum_of_credits + attempt.credits , filter(lambda item: item.grade > 0, courses), 0)

def average(courses: list):
    return  reduce(lambda average_of_grade, attempt: average_of_grade + attempt.grade , filter(lambda item: item.grade > 0, courses), 0) / len(list(filter(lambda item: item.grade > 0, courses)))

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)