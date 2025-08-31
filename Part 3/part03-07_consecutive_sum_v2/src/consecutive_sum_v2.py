# Write your solution here

limit = int(input("Limit:"))

addition = 0
count = 1
string = ""
while addition < limit:
    addition += count 
    string += f"{count}"
    count += 1
    
    if addition < limit:
        string += " + " 
    
     
string1 = "The consecutive sum: "
string2 = f" = {addition}"
string_final = string1 + string + string2
print(string_final)