from math import sqrt

def is_prime(n, i=None):
    if n <= 1:
        return False
    if i is None:
        i = int(sqrt(n))
    if i == 1:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i - 1)

def prime_numbers():
    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1

if __name__ == "__main__":
    numbers = prime_numbers()
    for _ in range(8):
        print(next(numbers))
