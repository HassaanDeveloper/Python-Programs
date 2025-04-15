# Import random module for generating random numbers
import random

# Number of sides on each die
num_sides = 6

def simulate_dice_roll():
    """Simulates rolling two dice and prints the results"""
    # Generate random numbers for each die
    dice1: int = random.randint(1, num_sides)
    dice2: int = random.randint(1, num_sides)
    # Calculate total of both dice
    total: int = dice1 + dice2
    # Print results
    print(f"Dice1 : {dice1}, Dice2 : {dice2}, Total: {total}")

def main():
    """Main function to demonstrate dice rolling simulation"""
    # Initialize dice1 variable
    dice1: int = 10
    print("dice1 in main()" + str(dice1))
    # Simulate rolling dice three times
    simulate_dice_roll()
    simulate_dice_roll()
    simulate_dice_roll()
    # Show dice1 value is unchanged
    print("dice1 in main()" + str(dice1))

# Execute simulate_dice_roll() if this file is run directly
if __name__ == "__main__":
    simulate_dice_roll()