#Allow a user to enter a quantity of an item. If the quantity is greater than or equal
#to 1000, the unit price should be $3.00. For quantities under 1000 the unit price is
#$5.00. Compute extended price to be quantity x unit price. Compute tax to be 7%
#of the extended price. The total is computed as extended price plus the tax.
#Display the quantity, unit price, extended price, tax and total.

#Input
qty = int(input("Enter the total number of the items: ")) 

#Process
if qty >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00
extended_price = qty * unit_price
tax = extended_price * 0.07  #representing 7% tax
total = extended_price + tax

#Output
print ()
print("Quantity: ", qty)
print("Unit Price: $", round(unit_price, 2))
print("Extended Price: $", round(extended_price, 2))
print("Tax: $", round(tax, 2))
print("Total: $", round(total, 2))