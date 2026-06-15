#Create a text file with item, quantity and price. Read through the file one line at a time. Compute
#the extended price (quantity x price). For each line display the item, quantity, price and extended
#price. After the loop display the sum of all the extended prices, the count of the number of orders
#and the average order

#Input
sum_of_extended_prices = 0.00
order_count = 0
f = open("Users/LaraClarissa/Documents/CIS106/M8P4.txt", "r")
item = f.readline()

#Process
while item != "":
    quantity = int(f.readline())
    price = float(f.readline())
    extended_price = quantity * price

    print("Item: ", item)
    print("Quantity: ", quantity)
    print("Price: $", round(price, 2))

    order_count = order_count + 1
    sum_of_extended_prices = sum_of_extended_prices + extended_price


    item = f.readline()

average_order = sum_of_extended_prices / order_count

#Output
print()
print("Sum of Extended Prices: $", round(sum_of_extended_prices, 2))
print("Count of Orders: ", order_count)
print("Average Order: $", round(average_order, 2))

