#The input to the problem is quantity of widgets. Your program should determine
#the price to charge based on the schedule below. Calculate the extended price
#(quantity x price). Calculate tax at 7%. Display the extended price, tax amount
#and total.
#Quantity Price
#>10000 $10
#5000 to 10000 $20
#Below 5000 $30

#Input
qty = int(input("Enter the number of widgets: ")) 

#Process
if qty > 10000:
    unit_price = 10
elif 5000 <= qty <= 10000:
    unit_price = 20
else:
    unit_price = 30
extended_price = qty * unit_price
tax = extended_price * 0.07
total = extended_price + tax

#Output
print ()
print("Extended Price: $", round(extended_price, 2))
print("Tax: $", round(tax, 2))
print("Total: $", round(total, 2))



