def add_many_numbers(numbers) -> int:
    """
    Calculates the sum of all numbers in the given list
    Args:
        numbers: List of integers to sum
    Returns:
        int: The sum of all numbers in the list
    """
    # Initialize running total
    total_so_far: int = 0
    # Add each number to the total
    for number in numbers:
        total_so_far += number
    return total_so_far

def main():
    # Create list of numbers to sum
    numbers: list[int] = [3, 9, 56, 99, 34]
    # Calculate sum of numbers
    sum_of_numbers: int = add_many_numbers(numbers)
    # Print result
    print(f"The sum of the numbers is: {sum_of_numbers}")

if __name__ == "__main__":  
    main()