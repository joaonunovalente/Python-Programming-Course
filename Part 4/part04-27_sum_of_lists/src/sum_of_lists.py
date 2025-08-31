# Write your solution here

def list_sum (a : list, b : list):
    result = []
    for n in range(0, len(a)):
        result.append(a[n] + b[n])
    return result




if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    list_sum (a, b)