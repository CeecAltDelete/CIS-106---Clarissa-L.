#You and two friends completed a job and received an amount that is entered into the problem.
#You are to split the amount received evenly between the three of you. Compute and display
#what each of you will receive.

#Input
total_amount = float(input("Enter total amount received: $"))

#Process
amount_per_person = total_amount / 3

#Output
print()
print("Each person will receive: $", round(amount_per_person, 2))