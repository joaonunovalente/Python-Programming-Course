# Write your solution here

def histogram(word: str):

    characters = {}     # Initalizing the dictionary
    for letter in word:
        if letter not in characters:
            characters[letter] = 1
        else:
            characters[letter] = characters[letter] + 1

    # Priting
    for key, value in characters.items():
        print(key, end=" ")
        print("*" * value)
       

if __name__ == "__main__":
    histogram("statistically")