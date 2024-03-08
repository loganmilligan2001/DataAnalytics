def get_user_info():
    username = input("Enter your username: ")
    full_name = input("Enter your full name: ")
    title = input("Enter your title (Dr, Mrs, Mr, etc.): ").upper()
    password = input("Enter your password: ")
    age = input("Enter your age: ")
    email = input("Enter your email address: ")

    # Convert the first letter of each name in full name to uppercase
    full_name = ' '.join(word.capitalize() for word in full_name.split())

    # Check if password is all digits
    if not password.isdigit():
        print("Password must contain only digits.")
        return None

    # Check if age is a digit
    if not age.isdigit():
        print("Age must be a number.")
        return None

    return {
        "username": username,
        "full_name": full_name,
        "title": title,
        "password": password,
        "age": int(age),
        "email": email
    }

user_info = get_user_info()
if user_info:
    print("User information:")
    for key, value in user_info.items():
        print(f"{key}: {value}")

