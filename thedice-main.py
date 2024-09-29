import random

print("Welcome to TheDice.")
roll = input("Press A or a to roll the dice : ")
faces = int(input("Enter a number of faces to roll (classic dices haves 6) : "))

while roll == "A" or roll == "a":
    roll = ""
    dice_roll_number = random.randint(1, faces)
    print("Your Diceroll result is " + str(dice_roll_number))
    roll = input("Press A or a to re-roll the dice or Q or q to quit : ")
    faces = int(input("Enter a number of faces to roll (classic dices haves 6) : "))

    if roll == "Q" or roll == "q":
        quit()
else:
    print("Please press A or a to roll.")
    quit()