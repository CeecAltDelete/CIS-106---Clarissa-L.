#Allow the user to enter the stock ticker symbol (ie MSFT for Microsoft), number of shares and
#cost per share. Compute and display amount invested to be number of shares times cost per
#share.

#Input
ticker = input("Enter the stock ticker symbol: ")
shares = int(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))

#Process
amount_invested = shares * cost_per_share

#Output
print("The amount invested in", ticker, "is: $", amount_invested)