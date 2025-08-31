import copy


def read_datafile(filename:str) -> dict:
    dictionary = {}
    temp_list = []

    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            if line != "":
                temp_list.append(line)
            else:
                dictionary[temp_list[0]] = temp_list[1:]
                temp_list = []
        dictionary[temp_list[0]] = temp_list[1:]
    
    return dictionary


def search_by_name(filename: str, word: str):
    recipes_dict = read_datafile(filename)
    found_recipes = []

    for key, value in recipes_dict.items():
        key_copy = copy.deepcopy(key)
        if word.lower() in key_copy.lower():
            found_recipes.append(key)
    
    return found_recipes


def search_by_time(filename: str, prep_time: int):
    recipes_dict = read_datafile(filename)
    found_recipes = []

    for key, value in recipes_dict.items():
        temp_list = []
        if int(value[0]) <= prep_time:
            temp_list.append(key)
            temp_list.append(value[0])
            found_recipes.append(f"{key}, preparation time {value[0]} min")

    return found_recipes


def search_by_ingredient(filename: str, ingredient: str):

    recipes_dict = read_datafile(filename)
    found_recipes = []

    for key, value in recipes_dict.items():
        temp_list = []
        for item in value:
            if ingredient == item:
                temp_list.append(key)
                temp_list.append(value[0])
                found_recipes.append(f"{key}, preparation time {value[0]} min")

    return found_recipes


if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")

    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_time("recipes1.txt", 20)

    for recipe in found_recipes:
        print(recipe)
    
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)


