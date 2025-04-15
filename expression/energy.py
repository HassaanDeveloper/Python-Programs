# Speed of light in meters per second
c: int = 299792458

def main():
    # Get mass input from user in kilograms
    mass: float = float(input("Enter mass in kg: "))
    # Calculate energy using E = mc^2 formula
    energy = mass * c ** 2

    # Print the equation
    print("e = mc^2")
    # Print the mass value
    print("m =" + str(mass) + " kg")
    # Print the speed of light
    print("c =" + str(c) + " m/s")
    # Print the calculated energy in Joules
    print(str(energy) + " Joules of energy")

# Execute main() if this file is run directly
if __name__ == "__main__":
    main()