# Write your solution here

def invert(s: dict):
    keys = []
    values = []

    for key, value in s.items():
        keys.append(key)
        values.append(value)
    
    s.clear()
    print(s)
    print(keys)

    for n in range(0, len(keys)):
        s[values[n]] = keys[n]

    print(s)



if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)