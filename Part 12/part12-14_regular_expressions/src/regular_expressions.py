# Write your solution here
import re

def is_dotw(input_string: str):
    expression = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    if re.search(expression, input_string):
        return True
    else:
        return False

def all_vowels(input_string: str):
    expression = "^[aeiou]*$"
    if re.search(expression, input_string):
        return True
    else:
        return False
    
def time_of_day(input_string: str):
    expression = "^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"
    if re.search(expression, input_string):
        return True
    else:
        return False

if __name__ == "__main__":
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))