#Prompt the user to repeatedly to do the program (input (Yes or No)). If they response Yes go
#into the loop and prompt the user for make, model, electric vehicle code (Y or N) and MSRP
#(sticker price) of an automobile. Write a function to compute the out the door price. Pass to the
#function the MSRP, make, model and electric vehicle code. Determine the percent off the MSRP
#then compute the new MSRP and finally add 7% sales tax to the total. Return and display the
#total. Also sum all MSRP’s and sum of all sales price of the cars (MSRP – discount + tax).
#To determine percent off MSRP Percent off MSRP
#Honda Accord 0.10
#Toyota Rav4 0.15
#All electric vehicles 0.30
#All other vehicles 0.05

#Input
def compute_out_the_door_price(msrp, make, model, electric_vehicle_code):
    if make.lower() == "Honda" and model.lower() == "Accord":
        discount_percent = 0.10
    elif make.lower() == "Toyota" and model.lower() == "Rav4":
        discount_percent = 0.15
    elif electric_vehicle_code.upper() == "Y":
        discount_percent = 0.30
    else:
        discount_percent = 0.05

    discounted_msrp = msrp * (1 - discount_percent)
    out_the_door_price = discounted_msrp * 1.07
    return out_the_door_price
#Process
answer = "yes"
sum_msrp = 0
sum_sales_price = 0
while answer.lower() == "yes" or answer.lower() == "y":
    make = input("Enter make: ")
    model = input("Enter model: ")
    electric_vehicle_code = input("Enter electric vehicle code (Y or N): ")
    msrp = float(input("Enter MSRP: "))

    out_the_door_price = compute_out_the_door_price(msrp, make, model, electric_vehicle_code)
    sum_msrp += msrp
    sum_sales_price += out_the_door_price
    print()
    print(f"Out the door price: {out_the_door_price:.2f}")
    print()
    answer = input("Do you want to enter another record? (Yes or No): ")

#Output
print()
print(f"Sum of MSRP: {sum_msrp:.2f}")
print(f"Sum of sales price: {sum_sales_price:.2f}")
print("Program finished.")