def add_three_copies(list, data):
    """
    Adds three copies of the given data to the list
    Args:
        list: The list to add copies to
        data: The data to copy into the list
    """
    # Add data to list 3 times
    for i in range(3):
        list.append(data)

def main():
    # Get message from user to copy
    message = input("Enter the meesage to copy: ")
    
    # Create empty list
    list = []
    
    # Print list before adding copies
    print("List before", list)
    
    # Add three copies of message to list
    add_three_copies(list, message)
    
    # Print list after adding copies
    print("List after", list)

if __name__ == "__main__":
    main()