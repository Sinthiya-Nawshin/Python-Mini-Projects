# Generates the amount of bill for each person after calculating the tip.

print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 0r 15? "))
person = int(input("How many people to split the bill? "))

tip_count = tip_percentage / 100 * total_bill + total_bill
payable_amount = tip_count / person
final_amount = round(payable_amount, 2)

print(f"Each person should pay: ${final_amount}")
