#Enter a part number and quantity Determine the cost per unit using the table
#below. Then calculate the total cost (quantity x unit cost). Display the part
#number, cost per unit and total cost. Note: Part number can be an integer but it can
#also be a string because you are not doing arithmetic on it. However, in your code
#if statement be sure to compare using consistency, that is, if item == “10” when
#item is a string and if item == 10 when item is an integer.
#Part Unit Cost
#10 or 55 1.00
#99 2.00
#80 or 70 3.00
#All others 5.0

#Input
part_number = input("Enter the part number: ")
quantity = int(input("Enter the quantity: "))

#Process
if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00
total_cost = quantity * unit_cost

#Output
print ()
print("Part Number: ", part_number)
print("Cost per Unit: $", round(unit_cost, 2))
print("Total Cost: $", round(total_cost, 2))

