# This program converts temperature from Fahrenheit to Celsius.

def main():
    degree_fahrenhite: float = float(input("Enter temperature in Fahrenheit: "))
    degree_celcius: float = (degree_fahrenhite - 32) * 5 / 9
    print(f"The temperature in Celsius is {degree_celcius:.2f}°C")

if __name__ == "__main__":
    main()