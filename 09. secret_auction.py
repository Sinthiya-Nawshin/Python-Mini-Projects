logo = '''                                                                                    
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to Secret Auction Program!")

def highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_number = bidding_dictionary[bidder]
        if bid_number > highest_bid:
            highest_bid = bid_number
            winner = bidder

    print(f"{winner} is the highest bidder with ${highest_bid}.")

bid_info = {}

continue_bidding = True

while continue_bidding:
    name = input("What is your name? : ")
    price = int(input("What is your bid? : $"))

    bid_info[name] = price

    should_continue = input("Are there any other bidders? Type 'Yes' or 'No' :\n").lower()

    if should_continue == "no":
        continue_bidding = False
        highest_bidder(bid_info)
    elif should_continue == "yes":
        print("\n" * 20)
