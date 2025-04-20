# This program creates a phonebook where the user can enter names and numbers.
def read_phone_numbers():
    """
    Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook.
    """

    phonebook = {}

    while True:
        name = input("Enter a name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number
    return phonebook

def print_phone_numbers(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))

def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter a name to look up: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook.")
        else:
            print(phonebook[name])

def main():
    """
    Ask the user to input names and numbers and store them in a dictionary.
    Once they enter a blank line, print out the phonebook.
    Then ask the user to look up names in the phonebook.
    """
    phonebook = read_phone_numbers()
    print_phone_numbers(phonebook)
    lookup_numbers(phonebook)

if __name__ == "__main__":
    main()