import random

print(" Welcome to Dice Roller!\n")

while True:
    input("Press Enter to roll the dice...")
    roll = random.randint(1, 6)
    print(f"\nYou rolled: {roll}\n")

    if roll == 6:
        print("Congratulations! You rolled the lucky 6!\n")

    replay = input("Do you want to roll again? yes/no: ").lower()
    print()
    if replay != "yes":
        print("Thanks for playing!")
        break
