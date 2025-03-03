import urllib.request
import json
import math

def retrieve_all():
    file_path = 'https://studies.cs.helsinki.fi/stats-mock/api/courses'
    my_request = urllib.request.urlopen(file_path)
    data: str = my_request.read()

    courses: list = json.loads(data)
    active_courses: list = []
    print(courses)

    for course in courses:
       if course['enabled']:
            fullName: str = course['fullName']
            name: str = course['name']
            year: int = course['year']
            exercises: int = sum(course['exercises'])   
            
            active_course: tuple = (fullName, name, year, exercises)
            active_courses.append(active_course)

    return active_courses


def retrieve_course(course_name: str):
    file_path = 'https://studies.cs.helsinki.fi/stats-mock/api/courses/' + course_name + '/stats'
    my_request = urllib.request.urlopen(file_path)
    data: str = my_request.read()
    course: list = json.loads(data)

    weeks: int = len(course)
    students: int = 0
    hours: int = 0
    hours_average: int = 0
    exercises: int = 0
    exercises_average: int = 0
    
    for _, values in course.items():
        if values['students'] > students:
            students = values['students']
        hours += values['hour_total']
        hours_average = math.floor(hours / students)
        exercises += values['exercise_total']
        exercises_average = math.floor(exercises / students)
        
    my_dict: dict = {
        'weeks': weeks, 
        'students': students, 
        'hours': hours,
        'hours_average': hours_average,
        'exercises': exercises,
        'exercises_average': exercises_average
        }

    return my_dict


if __name__ == "__main__":
    retrieve_all()
    retrieve_course("docker2019")
