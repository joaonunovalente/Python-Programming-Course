# Write your solution here

def create_tuple(x: int, y: int, z: int) -> tuple:
    numbers = (x, y, z)

    return (min(numbers), max(numbers), sum(numbers))


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))