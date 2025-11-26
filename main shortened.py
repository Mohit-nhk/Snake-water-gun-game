import random

# Input from user
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
# Random choice for computer
computer = random.choice([-1, 0, 1])
# Mapping values
youdict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Validate input
if youstr not in youdict:
    print("Invalid input. Please enter 's', 'w', or 'g'.")
else:
    #Value that user gets compared from dict and assigned to you
    you = youdict[youstr]

    # Show choices
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    # Determine result
    if computer == you:
        print("It's a draw")
    elif (computer == -1 and you == 1) or \
         (computer == 0 and you == -1) or \
         (computer == 1 and you == 0):                                              
        print("🎉 You win!")
    else:
        print("💻 You lose!")