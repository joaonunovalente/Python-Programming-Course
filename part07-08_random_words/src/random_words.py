from random import shuffle


def read_data() -> list:
    word_list = []
    with open("words.txt") as f:
        for line in f:
            line = line.strip()
            word_list.append(line)
    return word_list


def words(n: int, beginning: str) -> list:
    word_list = read_data()
    my_list = []
    for word in word_list:
        if word.startswith(beginning):
            my_list.append(word)
    
    shuffle(my_list)

    if n > len(my_list):
        raise ValueError('Not enough words.')

    return my_list[:n]


if __name__ == "__main__":
    read_data()
    word_list = words(500, "car")
    for word in word_list:
        print(word)