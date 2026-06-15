#The user will enter employee last name, salary and job level (as noted below). Use
#the job level to determine the bonus rate. Then compute bonus to be salary times
#bonus rate. Display employee last name and bonus.
#Job Level Bonus Rate
#10 and above 25%
#5 to 9 20%
#All others 10%

#Input
last_name = input("Enter employee last name: ")
salary = float(input("Enter employee salary: "))
job_level = int(input("Enter employee job level: "))

#Process
if job_level >= 10:
    bonus_rate = 0.25
elif 5 <= job_level <= 9:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10
bonus = salary * bonus_rate

#Output
print("Employee Last Name: ", last_name)
print("Bonus: $", round(bonus, 2))
print("Bonus Rate: ", round(bonus_rate * 100, 2), "%")

