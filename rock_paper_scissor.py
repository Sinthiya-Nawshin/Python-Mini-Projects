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

print(game_images[my_choice])

stuff = ["rock", "paper", "scissors"]
stuff_index = random.randint(0, 2)

print(f"Computer chose {stuff[stuff_index]}.")
print(game_images[stuff_index])

if my_choice == stuff_index:
    print("It's a tie!")
elif my_choice >= stuff_index:
    print("You chose an invalid number!")
elif my_choice == 0 and stuff_index == 1:
    print("You lose!")
elif my_choice == 0 and stuff_index == 2:
    print("You win!")
elif my_choice == 1 and stuff_index == 0:
    print("You lose!")
elif my_choice == 1 and stuff_index == 2:
    print("You win!")
elif my_choice == 2 and stuff_index == 0:
    print("You lose!")
elif my_choice == 2 and stuff_index == 1:
    print("You win!")

