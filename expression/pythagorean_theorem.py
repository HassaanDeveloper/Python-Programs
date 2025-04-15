import math

def main():
    """Main function to calculate the hypotenuse of a right triangle"""
    # Get user input for the lengths of the two sides
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))
    
    # Calculate the hypotenuse using the Pythagorean theorem
    bc: float = math.sqrt(ab**2 + ac**2)
    
    # Print the result
    print(f"The length of the hypotenuse is {bc:.2f}")\
    
if __name__ == "__main__":
    main()