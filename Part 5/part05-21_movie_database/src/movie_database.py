# Write your solution here

def  add_movie(database: list, name: str, director: str, year: int, runtime: int):
    my_dictionary =  {}
    my_dictionary["name"] = name
    my_dictionary["director"] = director
    my_dictionary["year"] = year
    my_dictionary["runtime"] = runtime

    database.append(my_dictionary)
    

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)