def check_voting_eligibility(name, age, registered):
    if age < 18:
        print(f"Sorry {name}, you are too young to vote.")
        print("You need to be at least 18 years old to vote.")
    elif not registered:
        print(f"Hello {name}! You are eligible to vote.")
        print("If you're not registered to vote, you can register at your local election office.")
        print("Please visit https://www.usa.gov/register-to-vote to find more information.")
    else:
        print(f"Hello {name}! You are eligible to vote.")
        print("You are already registered to vote.")
        print("You can go to your designated polling place on Election Day to cast your vote.")

def main():
    name = input("Enter your name: ")
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid age. Please enter a valid number.")
        return

    if age >= 18:
        registered = input("Are you registered to vote? (yes/no): ").lower() == 'yes'
    else:
        registered = False

    check_voting_eligibility(name, age, registered)

if __name__ == "__main__":
    main()