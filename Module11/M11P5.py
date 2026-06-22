#The input consists of quantity, price and discount rate. Use a function to compute the discount
#amount and discounted price. Then, display these values in the main part of the program, along
#with the quantity and price. (The function should return both discount amount and discounted
#price

#Input
def compute_discount(quantity, price, discount_rate):
    total = quantity * price
    discount_amount = total * discount_rate
    discounted_price = total - discount_amount
    return discount_amount, discounted_price

#Process
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
discount_rate = float(input("Enter discount rate (in decimal form): "))

discount_amount, discounted_price = compute_discount(quantity, price, discount_rate)

#Output
print()
print(f"Quantity: {quantity}")
print(f"Price: {price:.2f}")
print(f"Discount Amount: {discount_amount:.2f}")
print(f"Discounted Price: {discounted_price:.2f}")