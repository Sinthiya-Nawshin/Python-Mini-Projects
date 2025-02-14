import random

logo = r'''
.------.        88          88                       88        88                       88                
|( \/ ).-----.  88          88                       88        ""                       88        
| \  /|K /\  |  88          88                       88                                 88      
|  \/ | /  \ |  88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8    
`-----| \  / |  88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"  
      |  \/ K|  88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[                                             
      `------'  88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,
                8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a
                                                               88
                                                            888P"                
'''

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and returns the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose! Opponent has Blackjack."
    elif u_score > 21:
        return "You went over. Computer won."
    elif u_score == 0:
        return "You win with a Blackjack."
    elif c_score > 21:
        return "Computer went over. You won!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
       user_cards.append(deal_card())
       computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your score: {user_cards}, current score = {user_score}.")
        print(f"Computer's First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to plat a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 20)
    play_game()
