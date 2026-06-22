#Enter players last name, number of hits and at bats at the keyboard. Use a function to compute
#batting average. Pass the hits and at bats to the function. The function should return batting
#average. Display last name and batting average. Give a count of the number of players entered

#Input
def compute_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0  # Avoid division by zero
    return hits / at_bats

#Process
answer = "yes"
player_count = 0
while answer.lower() == "yes" or answer.lower() == "y":    
    last_name = input("Enter player's last name: ")
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at bats: "))
    batting_average = compute_batting_average(hits, at_bats)
    print()
    print(f"Player: {last_name}")
    print(f"Batting Average: {batting_average:.3f}")
    print()
    player_count += 1
    answer = input("Do you want to enter another player? (Yes or No): ")

#Output
print()
print(f"Total number of players entered: {player_count}")