def new_person(name: str, age: int) -> tuple:
    """Returns a tuple with the arguments inputed"""
    if name == "":
        raise ValueError("The name is empty.")
    elif len(name) >= 40:
        raise ValueError("Name is less than 40 characters.")
    elif len(name.split(" ")) < 2:
        raise ValueError("There is only one name. There should be at least two.")
    elif age < 0:
        raise ValueError("The age must be a positive number")
    elif age > 150:
        raise ValueError("Age must be under 150.")
    else:
        return (name, age)
        

if __name__ == "__main__":
    print(new_person("João Valente", 25))
