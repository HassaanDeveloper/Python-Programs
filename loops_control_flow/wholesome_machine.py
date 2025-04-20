Affirmation = "I am capable of doing anything I set my mind to."

def main():
    print("Type this affirmation: " + Affirmation)

    user_type = input()

    while user_type != Affirmation: # While the user's input isn't the affirmation
        # Tell the user that they did not type the affirmation correctly
        print("Incorrect. Try again.")
        # Ask the user to type the affirmation again!
        user_type = input("Type this affirmation: " + Affirmation)
        print()
    print("Congratulations! You typed the affirmation correctly.")
    print("You are amazing and capable of achieving great things!")

if __name__ == "__main__":
    main()