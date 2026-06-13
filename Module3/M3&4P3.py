#The student will enter their last name, midterm and final exam scores (0 – 100 points). Compute
#the total exam points to be the sum of 40% of midterm and 60% of the final exam. Display
#student last name and total exam points.

#Input
last_name = input("Enter your last name: ")
midterm_score = float(input("Enter your midterm exam score (0-100): "))
final_score = float(input("Enter your final exam score (0-100): "))

#Process
total_exam_points = (midterm_score * 0.4) + (final_score * 0.6)

#Output
print()
print(last_name,", your total exam points are:", total_exam_points)