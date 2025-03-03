def palindromes(word : str):
    word_inverse = ""
    for n in range(len(word), 0, -1):
        word_inverse += (word[n - 1])

    if word != word_inverse:
        print("that wasn't a palindrome")
        return False
    else:
        print(word, "is a palindrome!")
        return True



result = False
while not result:
    word = input("Please type in a palindrome: ")
    result = palindromes(word)
        


        