# Write your solution here
def factorials(n: int) -> dict:
    k = {}
    k[1] = 1

    for i in range(2, n + 1):
        k[i] = k[i - 1] * i


    return k

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])