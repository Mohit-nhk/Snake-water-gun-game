
'''
1 for snake
-1 for water
0 for gun



The backslash tells Python:
“This statement continues on the next line.”
Without it, Python would think the elif statement ends at the end of the first line, and would raise a syntax error.
Why is it used here?
To improve readability by splitting a long logical condition across multiple lines.
'''
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
    if (computer == you):
        print("It's a draw")
    else:
        if (computer == -1 and you == 1):
            print("You win!")
        elif (computer == -1 and you == 0):
            print("You lose!")
        elif (computer == 1 and you == -1):
            print("You lose!")
        elif (computer == 1 and you == 0):
            print("You win!")
        elif (computer == 0 and you == -1):
            print("You win!")
        elif (computer == 0 and you == 1):
            print("You lose!")
        else:
            print("Something went wrong!")


