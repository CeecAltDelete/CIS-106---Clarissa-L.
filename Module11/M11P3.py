#Prompt the user to repeatedly to do the program input (Yes or No)). If they respond Yes, go into
#the loop and prompt them for last name, month and sales. Write a function to compute next
#month’s forecast. Pass to the function month and sales. Determine the forecast percent (see
#below) and compute next month’s sales to be sales x (1+forecast percent). Return next month’s
#sales and display the value.
#Month Forecast Percent
#Jan, Feb, Mar 0.10
#Apr, May, Jun 0.15
#Jul, Aug, Sep 0.20
#Oct, Nov, Dec 0.25

#Input
def compute_forecast(month, sales):
    month = month.lower()
    if month in ['jan', 'feb', 'mar']:
        forecast_percent = 0.10
    elif month in ['apr', 'may', 'jun']:
        forecast_percent = 0.15
    elif month in ['jul', 'aug', 'sep']:
        forecast_percent = 0.20
    elif month in ['oct', 'nov', 'dec']:
        forecast_percent = 0.25
    else:
        print("Invalid month")
        exit()
    
    next_month_sales = sales * (1 + forecast_percent)
    return next_month_sales

#Process
answer = "yes"
while answer.lower() == "yes" or answer.lower() == "y":
    last_name = input("Enter last name: ")
    month = input("Enter month: ")
    sales = float(input("Enter sales: "))
    
    next_month_sales = compute_forecast(month, sales)
    
    print()
    print(f"Last Name: {last_name}")
    print(f"Next Month's Sales Forecast: {next_month_sales:.2f}")
    print()
    
    answer = input("Do you want to enter another record? (Yes or No): ")

#Output
print()
print("Program finished.")