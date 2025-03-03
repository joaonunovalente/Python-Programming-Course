def search_dictionary(search_word: str):
    words_found = []
    with open("dictionary.csv") as file:
        for line in file:
            line = line.strip()
            pair = line.split(";")
            if search_word in pair[0] or search_word in pair[1]:
                words_found.append(pair)

    for pair in words_found:
        print(f"{pair[0]} - {pair[1]}")


def write_dictionary(word_fi: str, word_en: str):
    with open("dictionary.csv", "a") as file:
        file.write(f"{word_fi};{word_en}\n")
    print("Dictionary entry added")


def main():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        option = int(input("Function: "))
        if option == 1:
            finnish_word = input("The word in Finnish: ")
            english_word = input("The word in English: ")
            write_dictionary(finnish_word, english_word)
        elif option == 2:
            search_word = input("Search term: ")
            search_dictionary(search_word)
        elif option == 3:
            print("Bye!")
            break


main()