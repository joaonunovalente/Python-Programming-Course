name = input("Whom should I sign this to: ")
filename = input("Where shall I save it: ")

message = f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"

with open(filename, "w") as file:
    file.write(message)