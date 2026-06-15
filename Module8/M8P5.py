#Create a text file with student last name, district code (I or O) and number of credits taken. Compute
#tuition owed (credits taken x cost per credit). Cost per credit for in district students (district code I) is
#250.00. Out of district students pay 500.00 per credit. For each line display student last name,
#credits taken and tuition owed. After the loop display sum of all tuition owed and the number of
#students

#Input
last_name = input("Enter student last name: ")
district_code = input("Enter district code (I for in-district, O for out-of-district): ")
credits_taken = int(input("Enter number of credits taken: "))

#Process
if district_code.upper() == "I":
    cost_per_credit = 250.00
elif district_code.upper() == "O":
    cost_per_credit = 500.00
else:
    print("Invalid district code. Please enter 'I' for in-district or 'O' for out-of-district.")
    cost_per_credit = 0.00
tuition_owed = credits_taken * cost_per_credit

#Output
print ()
print("Student Last Name: ", last_name)
print("Credits Taken: ", credits_taken)
print("Tuition Owed: $", round(tuition_owed, 2))

