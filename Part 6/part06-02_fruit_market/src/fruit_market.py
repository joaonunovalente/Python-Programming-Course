# write your solution here
def read_fruits() -> dict:
    dictionary = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            # print(parts)
            dictionary[parts[0]] = float(parts[1])
    print(dictionary)

    return dictionary

if __name__ == "__main__":
    read_fruits()
