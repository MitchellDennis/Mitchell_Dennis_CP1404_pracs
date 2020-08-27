
"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))


sale_bonus_cutoff = 1000

while sales >= 0:
    if sales < sale_bonus_cutoff:
        print(0.1 * sales)
    elif sales >= sale_bonus_cutoff:
        print(0.15 * sales)
    else:
        print("Invalid entry. Try again.")
    sales = float(input("Enter sales: $"))

print("Thanks")