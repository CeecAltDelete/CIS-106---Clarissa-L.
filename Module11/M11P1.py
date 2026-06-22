#Allow the user to enter quantities and prices in a loop. Use a function to compute the total
#(quantity times price). The function should be passed the quantity and price and then return the
#total. In the function, provide a 10% discount if the total is over $10,0000.00. Display quantity,
#price and total. Sum and display the total extended price.

#Input
def compute_total(quantity, price):
    total = quantity * price
    if total > 10000:
        total *= 0.9  # Apply a 10% discount
    return total

#Process
total_extended_price = 0
answer = "yes"
while answer.lower() == "yes" or answer.lower() == "y":
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    
    total = compute_total(quantity, price)
    total_extended_price += total
    
    print(f"Quantity: {quantity}, Price: {price:.2f}, Total: {total:.2f}")
    answer = input("Do you want to enter another item? (Yes or No): ")

#Output
print ()
print(f"Total Extended Price: {total_extended_price:.2f}")