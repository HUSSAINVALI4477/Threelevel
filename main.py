# Define the passwords for each level
passwords = {
    "level1": "password1",
    "level2": "password2",
    "level3": "password3"
}

def authenticate(level):
    # Prompt the user for a password
    entered_password = input(f"Enter the password for {level}: ")

    # Check if the entered password matches the stored password
    if entered_password == passwords.get(level):
        print(f"Access to {level} granted.")
    else:
        print(f"Access to {level} denied.")

def main():
    print("Welcome to the Three-Level Password Authentication System")

    # Choose the level to access
    while True:
        print("\nChoose a level to access:")
        print("1. Level 1")
        print("2. Level 2")
        print("3. Level 3")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            authenticate("level1")
        elif choice == "2":
            authenticate("level2")
        elif choice == "3":
            authenticate("level3")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
