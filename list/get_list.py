def main():
    # Initialize empty list to store elements
    lst = []
    
    # Get first element from user
    elem = input("Enter an element: ")
    
    # Keep getting elements until user enters empty string
    while elem != "":
        # Add element to list
        lst.append(elem)
        # Get next element
        elem = input("Enter an element: ")
    
    # Print the final list
    print("Here is the list:", lst)

if __name__ == "__main__":  
    main()