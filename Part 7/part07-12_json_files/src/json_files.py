import json


def print_persons(filename: str):
    
    with open(filename) as file:
        date: str = file.read()

    students: list = json.loads(date)

    message: str
    for dictionary in students:
        name = dictionary["name"]
        age = dictionary["age"]
        hobbies = dictionary["hobbies"]

        print(f"{name} {age} years ({', '.join(hobbies)})")


if __name__ == "__main__":
    filename: str = "file1.json"
    print_persons(filename)