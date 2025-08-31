# Write your solution here

editor = ""
while editor.lower() != "visual studio code":
    editor = input("Editor:")
    if editor.lower() == "notepad" or editor.lower() == "word":
        print("awful")
    else:
        if editor.lower() != "visual studio code":
            print("not good")
    

print("an excellent choice!")


