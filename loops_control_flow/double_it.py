# This program doubles a number until it reaches 100 or more
def main():

    curr_value = int(input("Enter a number: "))
    # Double the number
    while curr_value < 100:
        curr_value = curr_value * 2
        # Print the result
        print(curr_value, end=" ")
# Call the main function when "run"
if __name__ == "__main__":
    main()