import re


def read_data(filename: str = "words.txt") -> list:
    """Reads the data from text file and returns the list of words."""
    words = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            words.append(line)
            
    return words


def find_words(search_term: str) -> list:
    words = read_data()

    matches = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    

    for word in words:
        if search_term[0] == "*" and word.endswith(search_term[1:]):
            matches.append(word)
        elif search_term[-1] == "*" and word.startswith(search_term[:-1]):
            matches.append(word)
        elif "." in search_term:
            x = re.search(search_term, word)
            if re.search(search_term, word) != None:
                if len(search_term) == len(word):
                    matches.append(word)   
        else:
            if word == search_term:
                matches.append(word)

    return matches


if __name__ == "__main__":
    print(find_words("ca."))
