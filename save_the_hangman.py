import random
from words_module import word_list

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_guess = []

while game_over is False:
    print(f"***** {lives}/6 Lives are Left ******")
    guess_letter = input("Guess a letter: ").lower()

    if guess_letter in chosen_word:
        print(f"You guessed the letter {guess_letter}!")

    display = ""

    for letter in chosen_word:
        if letter == guess_letter:
            display += letter
            correct_guess.append(guess_letter)
        elif letter in correct_guess:
            display += letter
        else:
            display += "_"
    print(display)

    if guess_letter not in chosen_word:
        lives -= 1
        print(f"You guessed {guess_letter} which is not in the word. You lose a life!")
        print(stages[lives])
        if lives == 0:
            game_over = True
            print("You lose.")
    else:
        print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win!")
