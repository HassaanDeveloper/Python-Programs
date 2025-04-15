inches_in_feet: int = 12

def main():
    """Main function to convert feet to inches"""
    # Get user input for feet
    feet: float = float(input("Enter feet: "))
    # Calculate inches
    inches: float = feet * inches_in_feet
    # Print the result
    print("That it" + str(inches) + " inches")

if __name__ == "__main__":
    main()  