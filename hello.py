# hello.py

def greet_user():
    print("===================================")
    print("     Welcome to Hello Program      ")
    print("===================================\n")

    # Taking user input
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    # Displaying greeting
    print("\nHello,", name + "!")
    print("Nice to meet you 😊")

    # Simple logic
    try:
        age = int(age)
        if age < 18:
            print("You are quite young!")
        elif age < 60:
            print("You are an adult!")
        else:
            print("You are a senior citizen!")
    except ValueError:
        print("Invalid age entered.")

    print("\nThank you for using this program!")
    print("Have a great day 🚀")


# Main execution
if __name__ == "__main__":
    greet_user()