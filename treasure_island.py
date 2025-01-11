# Finding the treasure in an island by making the right choices.

img = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

print(img)

print("Welcome to the Treasure Island.\n Your mission is to find the treasure.")
left = input("You're at a crossroad. Which way do u wanna go? left or right? ").lower()

if left == "left":
    print("You have entered the 2nd stage.")
    wait = input("Do u wanna wait here or swim across the lake? ").lower()

    if wait == "wait":
        print("Great! Now wait for the doors to appear.")
        yellow = input("Which door do u wanna go through? red, blue, or yellow? ").lower()

        if yellow == "yellow":
            print("Congratulations! You have found the treasure.")
        elif yellow == "red" or yellow == "blue":
            print("Wrong door. Game over. GOODBYE!")
        else:
            print("No such door exists. Game over.")
    else:
        print("The treasure isn't in the lake. Game over.")
else:
    print("Um, you're dead. Game over.")
