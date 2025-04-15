"""
Program which takes two numbers as input in string and convert them in integer, then print their sum.
"""

def main():
    num1: str = input("Enter first number: ")
    num1: int = int(num1)
    num2: str = input("Enter second number: ")
    num2: int = int(num2)
    sum: int = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")

if __name__ == "__main__":
    main()