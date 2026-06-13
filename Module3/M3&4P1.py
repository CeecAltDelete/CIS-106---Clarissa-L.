#Allow the user to enter two exam scores from the keyboard. The first exam is worth 60% of the
#total points and the second exam is worth 40%. Calculate the total score by multiplying each
#exam score input by the respective weighting then add the two results together. Display the total.

#Input
exam1 = float(input("Enter the score for the first exam: "))
exam2 = float(input("Enter the score for the second exam: "))

#Process
total = (exam1 * 0.6) + (exam2 * 0.4)

#Output
print("The total score is:", total) 