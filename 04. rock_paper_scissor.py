# Playing rock, paper, scissors with random choice generator

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

my_choice = int(input("what do u choose? type 0 for rock, 1 for paper and 2 for scissors. \n"))

if my_choice == 0:
    print("You chose rock.")
elif my_choice == 1:
    print("You chose paper.")
elif my_choice == 2:
    print("You chose scissors.")

if 0 <= my_choice <= 2:
    print(game_images[my_choice])

choices = ["rock", "paper", "scissors"]
computer_choice = random.randint(0, 2)

print(f"Computer chose {choices[computer_choice]}.")
print(game_images[computer_choice])

if my_choice == computer_choice:
    print("It's a tie!")
elif my_choice >= 3 or my_choice < 0:
    print("You chose an invalid number!")
elif my_choice == 0 and computer_choice == 1:
    print("You lose!")
elif my_choice == 0 and computer_choice == 2:
    print("You win!")
elif my_choice == 1 and computer_choice == 0:
    print("You lose!")
elif my_choice == 1 and computer_choice == 2:
    print("You win!")
elif my_choice == 2 and computer_choice == 0:
    print("You lose!")
elif my_choice == 2 and computer_choice == 1:
    print("You win!")
    
