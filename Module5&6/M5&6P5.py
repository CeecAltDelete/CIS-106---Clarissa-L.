#Have the user to enter number of concert tickets. The price per ticket depends on
#the volume (see below). Display the number of tickets, price per ticket and the
#total cost (number of tickets x Price Per Ticket).
#Quantity Price Per Ticket
#>=25 $50
#10 to 24 $60
#5 to 9 $70
#Less than 5 $75

#Input
tickets = int(input("Enter the number of concert tickets: "))

#Process
if tickets >= 25:
    price_per_ticket = 50
elif 10 <= tickets <= 24:
    price_per_ticket = 60
elif 5 <= tickets <= 9:
    price_per_ticket = 70
else:
    price_per_ticket = 75
total_cost = tickets * price_per_ticket

#Output
print()
print("Number of Tickets: ", tickets)
print("Price per Ticket: $", round(price_per_ticket, 2))
print("Total Cost: $", round(total_cost, 2))

