def main():
    furits = {"apple": 1.5, "banana": 0.5, "orange": 0.75, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    total_cost = 0

    for furit_name in furits:
        price = furits[furit_name]
        amount_bought = int(input(f"How many {furit_name}s do you want to buy? "))
        total_cost += price * amount_bought;

    print(f"Total cost: {total_cost}")
    print("Thank you for shopping with us!")

if __name__ == "__main__":  
    main()