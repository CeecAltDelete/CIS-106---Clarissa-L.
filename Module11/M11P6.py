#Enter the student’s last name and 3 exam scores. Use a function to compute the average and
#total points. This function should return both total points and average. Display student’s last
#name, total points and average exam score

#Input
def compute_total_and_average(score1, score2, score3):
    total_points = score1 + score2 + score3
    average = total_points / 3
    return total_points, average

last_name = input("Enter last name: ")
score1 = float(input("First exam score: "))
score2 = float(input("Second exam score: "))
score3 = float(input("Third exam score: "))

#Process
total_points,average = compute_total_and_average(score1,score2,score3)

#Output
print()
print(f"{last_name}'s total score: {total_points}%")
print(f"{last_name}'s average score: {average:.2f}%")
