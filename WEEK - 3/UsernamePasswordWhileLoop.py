import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Generate a random username and password
username = "example_username"
password = generate_password()

# Save username and password to files
save_to_file('username.txt', username)
save_to_file('password.txt', password)

while True:
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    saved_username = read_from_file('username.txt')
    saved_password = read_from_file('password.txt')

    if entered_username == saved_username and entered_password == saved_password:
        print("Username and password correct.")
        print("Username:", entered_username)
        print("Password:", entered_password)
        break
    else:
        print("Incorrect username or password. Please try again.")