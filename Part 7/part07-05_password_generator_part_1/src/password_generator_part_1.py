from random import sample
from string import ascii_lowercase


def generate_password(password_length: int) -> str:
    password = "".join(sample(ascii_lowercase, password_length))
    return password


if __name__ == "__main__":
    print(generate_password(8))