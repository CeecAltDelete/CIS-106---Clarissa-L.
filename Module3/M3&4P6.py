#Input the purchase price per share, the current stock price and quantity of stock, compute the
#increase (or decrease) of the value of the stock entered. (Value is computed as (current price –
#price per share) * quantity. If the amount is negative that means you are losing money)

#Input
pp = float(input("Enter the purchase price: $"))
csp = float(input("Enter the current stock price: $"))
qty = int(input("Enter the stock quantity: "))

#Process
change_in_value = (csp - pp) * qty

#Output
print()
print("The change in the value of the stock is: $", round(change_in_value, 2))
if change_in_value > 0:
    print ("The change in the value of the stock is positive. You are making money.")
else: 
    print ("The change in the value of stock is negative. You are losing money.")