"""
Shop Calculator
"""

total_cost = 0              #used to sum up total cost
after_discount = 0.9        #used to determine the price after input (1-0.1)
verify_int_input = 0        #Used to determine if initial input is int

while verify_int_input < 1:
    try:
        no_of_items = int(input("Enter number of items: "))     #if a non-int is entered scips to except the continues to start of loop
        verify_int_input = 1                                    #If int is input verifys that input is correct and exits loop
    except ValueError:
        print("Not a valid number of inputs. (Must be an integer)")
        continue


for i in range(0, no_of_items, 1):                                      #counts from 0 to the total number of items input
    total_cost = total_cost + float(input("Enter price of item: $"))    #adds the next entered value to the total

if total_cost > 100:                                                    #checks if the total meets the specifications for the discount
    total_cost = total_cost * after_discount
else:
    pass


print("The total price for the {} is ${:.2f}".format(no_of_items,total_cost))   #prints the total price to 2 decimal places
