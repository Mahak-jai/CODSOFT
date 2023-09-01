import random
import string

def generate_password(length=22):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    password_length = int(input("Enter the desired password length: "))
    
    if (password_length < 6):
        print("Password length should be at least 6 characters.")
    else:
        password = generate_password(password_length)
        print("Generated Password:", password)

if (__name__ == "__main__"):
    main()
