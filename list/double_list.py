def main():
    # Create a list of integers
    numbers: list[int] = [2, 4, 6, 8, 10, 12]
    
    # Iterate through each index of the list
    for i in range(len(numbers)):
        # Get element at current index
        elem_at_index = numbers[i]
        # Double the element and store back in list
        numbers[i] = elem_at_index * 2
    
    # Print the modified list
    print(numbers)

if __name__ == "__main__":
    main()