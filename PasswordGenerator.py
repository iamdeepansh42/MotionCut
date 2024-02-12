import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    num_passwords = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter the length of each password: "))

    passwords = generate_multiple_passwords(num_passwords, length)

    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")
