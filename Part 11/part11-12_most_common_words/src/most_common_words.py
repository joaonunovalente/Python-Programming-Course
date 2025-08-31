def read_file(filename: str):
    with open(filename) as new_file:
        contents = new_file.read()
    
    return contents

def most_common_words(filename: str, lower_limit: int):
    contents = read_file(filename)
    contents = "".join([character for character in contents if character not in ".!,?:"])
    splitted  = {word: contents.split().count(word) for word in contents.split() if contents.split().count(word) >= lower_limit}
    return splitted

if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))