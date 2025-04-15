# This program calculates the quotient and remainder of two numbers.
def main():
    # Get the numbers we want to divide
    dividend = int(input("Enter the number to be divided: "))
    divisor = int(input("Enter the number to divide by: "))

    quotient = dividend // divisor
    remainder = dividend % divisor

    print("The result of this division is" + str(quotient) + "with a remainder of" + str(remainder) + ".")

if __name__ == "__main__":
    main()