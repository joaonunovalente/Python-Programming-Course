# Write your solution here

def  add_movie(database: list, name: str, director: str, year: int, runtime: int):
    my_dictionary =  {}
    my_dictionary["name"] = name
    my_dictionary["director"] = director
    my_dictionary["year"] = year
    my_dictionary["runtime"] = runtime

    database.append(my_dictionary)

    
def find_movies(database: list, search_term: str):
    search_term.lower()
    new_list = []
    for entry in database:
        if search_term in entry["name"].lower():
            new_list.append(entry)
    return new_list


if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)