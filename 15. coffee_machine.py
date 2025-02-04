coffee_logo = r""" 
$$$$$$\             $$$$$$\   $$$$$$\                           $$\      $$\                     $$\       $$\                     
$$  __$$\           $$  __$$\ $$  __$$\                          $$$\    $$$ |                    $$ |      \__|                    
$$ /  \__| $$$$$$\  $$ /  \__|$$ /  \__|$$$$$$\   $$$$$$\        $$$$\  $$$$ | $$$$$$\   $$$$$$$\ $$$$$$$\  $$\ $$$$$$$\   $$$$$$\  
$$ |      $$  __$$\ $$$$\     $$$$\    $$  __$$\ $$  __$$\       $$\$$\$$ $$ | \____$$\ $$  _____|$$  __$$\ $$ |$$  __$$\ $$  __$$\ 
$$ |      $$ /  $$ |$$  _|    $$  _|   $$$$$$$$ |$$$$$$$$ |      $$ \$$$  $$ | $$$$$$$ |$$ /      $$ |  $$ |$$ |$$ |  $$ |$$$$$$$$ |
$$ |  $$\ $$ |  $$ |$$ |      $$ |     $$   ____|$$   ____|      $$ |\$  /$$ |$$  __$$ |$$ |      $$ |  $$ |$$ |$$ |  $$ |$$   ____|
\$$$$$$  |\$$$$$$  |$$ |      $$ |     \$$$$$$$\ \$$$$$$$\       $$ | \_/ $$ |\$$$$$$$ |\$$$$$$$\ $$ |  $$ |$$ |$$ |  $$ |\$$$$$$$\ 
 \______/  \______/ \__|      \__|      \_______| \_______|      \__|     \__| \_______| \_______|\__|  \__|\__|\__|  \__| \_______|"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


print(coffee_logo)


def check_resources(order_ingredients):
    """Returns True if order can be made, False if ingredients insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there's not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from inserted coins."""
    print("Please insert coins.")
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many Dimes?: ")) * 0.1
    total += int(input("How many Nickels?: ")) * 0.05
    total += int(input("How many Pennies?: ")) * 0.01
    return total


def transaction_status(money_received, drink_cost):
    """Returns True if payment is accepted, False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the items."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}. ☕ Enjoy!")


system_continue = True

while system_continue:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("Coffee Machine is shutting down.")
        system_continue = False
    elif choice == "report":
        print("Showing available resources...")
        print(f"Water = {resources['water']}ml)")
        print(f"Milk = {resources['milk']}ml")
        print(f"Coffee = {resources['coffee']}g")
        print(f"Money = ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if transaction_status(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
