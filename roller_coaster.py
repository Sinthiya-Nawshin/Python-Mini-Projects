print("Welcome to the roller coaster")
height = int(input("Please enter your height in cm: "))
bill = 0
if height >= 120:
    print("You can ride the coaster!")
    age = int(input("Please enter your age in years: "))
    if age <= 12:
        bill = 5
        print("You have to pay $5")
    elif age <= 18:
        bill = 7
        print("You have to pay $7")
    elif 45 <= age <= 55:
        print("You get to ride free!")
    else:
        bill = 12
        print("You have to pay $12")

    photo = input("Do you want to take a photo? (yes/no): ")
    if photo == "yes":
        print("It costs additional $3.")
        bill += 3
    print(f"Your final bill is: ${bill}")

else:
    print("You are too young to ride")