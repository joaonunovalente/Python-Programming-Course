# Write your solution here

list = []       # List of strings

while True:
    word = input("Word: ")
    if word in list:
        print(f"You typed in {len(list)} different words")
        break
    list.append(word)

    
        
