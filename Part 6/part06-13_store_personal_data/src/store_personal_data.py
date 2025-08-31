# Write your solution here
def store_personal_data(person: tuple):
    filename = "people.csv"
    with open(filename, "a") as file:
        line = f"{person[0]};{person[1]};{person[2]}\n"
        file.write(line)

    return


if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))