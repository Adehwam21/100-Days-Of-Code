import string
import secrets
import random


def generate_password():
    length_of_password = int(input("Enter password length: "))
    chars = "~@#$%^&*(){}|:<>?-=[]\;/."
    source = string.ascii_letters + string.digits + chars
    random.shuffle(list(source))
    password = ''.join(secrets.choice(source) for _ in range(length_of_password))
    print(f"Your generated password: {password}")
    exit()

generate_password()
