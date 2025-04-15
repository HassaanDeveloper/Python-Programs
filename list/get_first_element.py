def get_first_elem(lst):
    """
    Prints the first element of the given list
    Args:
        lst: The list to get the first element from
    """
    print(lst[0]);

def get_lst():
    """
    Gets input from user to build a list of strings
    Returns:
        list: The list of strings entered by the user
    """
    # Initialize empty list
    lst = []

    # Get first element from user
    elem: str = input("Enter an element of the list or press enter to stop: ")
    # Keep getting elements until user enters empty string
    while elem != "":
        # Add element to list
        lst.append(elem)
        # Get next element
        elem = input("Enter an element of the list or press enter to stop: ")
    return lst

def main():
    # Get list from user
    lst = get_lst()
    # Print first element
    get_first_elem(lst)

if __name__ == "__main__":
    main()