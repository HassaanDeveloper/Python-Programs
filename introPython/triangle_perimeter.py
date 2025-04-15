# This program calculates the perimeter of a triangle given the lengths of its three sides.
def main():
    side1: float = float(input("Enter the length of first side of triangle: "))
    side2: float = float(input("Enter the length of second side of triangle: "))
    side3: float = float(input("Enter the length of third side of triangle: "))

    perimeter: float = side1 + side2 + side3
    print("The perimeter of the triangle is: " + str(perimeter))

if __name__ == "__main__":
    main()