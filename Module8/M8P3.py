#Create a text file that contains employee last name and salary. Read in this data. Determine the
#bonus rate based on the chart below. Use that rate to compute bonus. For each line display the
#employee’s last name, salary and bonus. After the loop display the sum of all bonuses paid out.
#Salary Bonus Rate
#100,000.00 and up 20%
#50,000.00 15%
#All other salaries 10%

#Input
f = open("Users/LaraClarissa/Documents/CIS106/M8P3.txt", "r")
sum_of_bonuses = 0.00
last_name = f.readline()

#Process
while last_name != "":
    salary = float(f.readline())
    
    if salary >= 100000.00:
        bonus_rate = 0.20
    elif salary >= 50000.00:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.10
    
    bonus = salary * bonus_rate
    
    #Output for each employee
    print ()
    print("Employee Last Name: ", last_name)
    print("Salary: $", round(salary, 2))
    print("Bonus: $", round(bonus, 2))
    print("Bonus Rate: ", round(bonus_rate * 100, 2), "%")
    
    sum_of_bonuses = sum_of_bonuses + bonus

    last_name = f.readline()

#Output
print ()
print("Sum of Bonuses: $", round(sum_of_bonuses, 2))
