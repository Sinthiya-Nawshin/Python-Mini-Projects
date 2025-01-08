print("Welcome to Python Pizza Shop!")

size = input("What size pizza do you want? S, M, or L? ")
pepperoni = input("Do you want pepperoni as topping? Y or N? ")
cheese = input("Do you want cheese on it? Y or N? ")
bill = 0

if size == "S":
    bill += 15

elif size == "M":
    bill += 20

elif size == "L":
    bill += 25

else:
    print("Sorry, not a valid size.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")