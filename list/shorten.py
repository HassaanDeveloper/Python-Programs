# Maximum allowed length of the list
MAX_LENGTH: int = 3

def shroten(lst):
    """
    Shortens the list by removing elements from the end until it reaches MAX_LENGTH
    Args:
        lst: The list to shorten
    """
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(f"Removed {last_elem} from the list")

def get_lst():
    """
    Gets input from user to build a list of strings
    Returns:
        list: The list of strings entered by the user
    """
    lst = []

    elem: str = input("Enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter an element of the list or press enter to stop: ")
    return lst

def main():
    # Get list from user and shorten it
    lst = get_lst()
    shroten(lst)

if __name__ == "__main__":
    main()