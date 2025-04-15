def main():

    year = int(input("Enter a year: "))
    # Check if the year is divisible by 4
    if year % 4 == 0 :
        if year % 100 == 0: # Checking whether the provided year is evenly divisibly by 100
            if year % 400 == 0: # Checking whether the provided year is evenly divisibly by 400
                print(year, "is a leap year!.")
            else:
                print(year, "is not a leap year.")
        else:
            print(year, "is a leap year!.")
    else:
        print(year, "is not a leap year.")

if __name__ == "__main__":
    main()