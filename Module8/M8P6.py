#Prompt the user on whether they want to do this program (just before the while loop). “Yes” entry
#means they want to continue. Any other response indicates they will stop the program. This
#response is the loop control variable. If the user answers “Yes “then go into the while loop
#Once in the while loop. You are to prompt the user for their last name and two exam scores.
#Compute the average exam score. Display last name and average. After the loop, display a count
#of the number of students who entered data

#Input
response = input("Do you want to enter student data? (Yes/No): ")
student_count = 0

#Process
while response.lower() == "yes":
    last_name = input("Enter student last name: ")
    exam_score1 = float(input("Enter first exam score: "))
    exam_score2 = float(input("Enter second exam score: "))
    
    average_score = (exam_score1 + exam_score2) / 2
    
    print()
    print("Student Last Name: ", last_name)
    print("Average Exam Score: ", round(average_score, 2))
    
    student_count = student_count + 1
    response = input("Do you want to enter student data? (Yes/No): ")


#Output
print()
print("Total number of students entered: ", student_count)

