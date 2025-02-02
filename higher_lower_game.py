import random
from game_data import data

logo = r'''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ /_/_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     '''

vs = r'''        
 _   _______
| | / / ___/
| |/ (__  ) 
|___/____/  
            '''

def check_ans(user_guess, followers_a, followers_b):
    """Takes user's guess, checks the follower count and returns it if they got it right."""
    if followers_a > followers_b:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
score = 0
game_continue = True

compare_b = random.choice(data)

while game_continue:
    compare_a = compare_b
    compare_b = random.choice(data)

    if compare_a == compare_b:
        compare_b = random.choice(data)

    print(f"Compare A: {compare_a["name"]}, a {compare_a["description"]}, from {compare_a["country"]}.")
    print(vs)
    print(f"Against B: {compare_b["name"]}, a {compare_b["description"]}, from {compare_b["country"]}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

# Comparing follower count
    follower_a = compare_a["follower_count"]
    follower_b = compare_b["follower_count"]

    is_correct = check_ans(guess, follower_a, follower_b)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continue = False

