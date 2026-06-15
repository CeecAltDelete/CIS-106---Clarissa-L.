#Enter a principle amount of a CD and year to maturity of CD. Determine the
#interest rate based on the amount of the principle and maturity (see below).
#Calculate first year interest (principle x interest rate). Display principle, interest
#rate and the interest amount for first year.
#Principle Years to Maturity Interest Rate
#>$100,000 5 6%
#$50,000 to $100,000 10 5%
#$50,000 to $100,000 5 4%
#Any other principle and years 2%

#Input
principle = float(input("Enter the principle amount of the CD: "))
years = int(input("Enter the years to maturity of the CD: "))

#Process
if principle > 100000 and years == 5:
    interest_rate = 0.06
elif 50000 <= principle <= 100000 and years == 10:
    interest_rate = 0.05
elif 50000 <= principle <= 100000 and years == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02
interest = principle * interest_rate

#Output
print ()
print("Principle: $", round(principle, 2))
print("Interest Rate: ", round(interest_rate * 100, 2), "%")
print("First Year Interest: $", round(interest, 2))



