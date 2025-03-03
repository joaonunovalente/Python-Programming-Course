# Write your solution here
def longest(words: list):
    longest_word = ""
    for word in words:
        if len(word) >= len(longest_word):
            longest_word = word

    return longest_word

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))