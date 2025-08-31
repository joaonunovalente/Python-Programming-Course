class Course:
    def __init__(self):
        self._course = None
        self._grade = None
        self._credits = None
    
    def add_course(self, course):
        self._course = course

    def add_grade(self, grade):
        self._grade = grade
    
    def add_credits(self, credits):
        self._credits = credits
    
class Statistics:
    pass

class ProgramExecution:
    def __init__(self):
        self.courses = []

    def help(self):
        print("0 exit")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
    
    def add_course(self):
        object = Course()
        course = input("course: ")
        object.add_course(course)
        grade = input("grade: ")
        object.add_course(grade)        
        credit = input("credit: ")
        object.add_course(credit)

    def execute(self):
        self.help()
        while True:
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                self.add_course()
            elif command == 2:
                self.add_course()
            elif command == 3:
                self.add_course()
            else:
                self.help()

program = ProgramExecution()
program.execute()