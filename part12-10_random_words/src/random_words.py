def word_generator(characters: str, length: int, amount: int):
    substrings = (characters[i : i + length] for i in range(amount))

    return substrings

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)