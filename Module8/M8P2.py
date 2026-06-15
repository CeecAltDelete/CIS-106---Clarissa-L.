#Allow the user to enter a start value, stop value and increment value from the keyboard. Display all
#the numbers from the start value to stop value using the increment value as you proceed. Use a
#while loop structure for this problem.

#Input
start_value = int(input("Enter your start value: "))
stop_value = int(input("Enter your stop value: "))
increment_value = int(input("Enter your increment value: "))

#Process
current_value = start_value
while current_value <= stop_value:
    print(current_value)
    current_value = current_value + increment_value

#Output
print()
print("All numbers from", start_value, "to", stop_value, "with an increment of", increment_value, "!")

