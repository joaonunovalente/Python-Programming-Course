word = input("Please type in a word: ")
character = input("Please type in a character: ") 
index = word.find(character)
while index!=-1:
    if len(word)>=index+3:
        print(word[index:index+3])
    index = word.find(character,index+1)
 

