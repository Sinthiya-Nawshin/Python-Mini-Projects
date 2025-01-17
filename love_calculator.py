# Calculating TRUE and LOVE strings in 2 parameters in a function and then adding them together.

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    true_count = 0
    for letters in "true":
        for char in combined_names:
            if char == letters:
                true_count += 1

    love_count = 0
    for letters in "love":
        for char in combined_names:
            if char == letters:
                love_count += 1

    love_score = int(str(true_count) + str(love_count))
    print(love_score)

calculate_love_score("Kim Kardashian", "Kanye West")