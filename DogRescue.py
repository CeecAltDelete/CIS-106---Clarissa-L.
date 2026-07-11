class Dog:
    def __init__(self, name, breed, age, weight):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight

def menu():
    print("Dog Rescue")
    print("----------")
    print("1 - Add a dog")
    print("2 - View dogs")
    print("3 - Find dogs")
    print("4 - Exit")

def addDog(dog_roster):
    name = input("Dog Name: ")
    breed = input("Dog Breed: ")
    age = input("Age: ")
    weight = input("Weight: ")

    new_dog = Dog(name, breed, age, weight)
    dog_roster.append(new_dog)
    print(f"{name} has been added.")
    print()

def viewDogs(dog_roster):
    if not dog_roster:
        print("No dogs have been added yet.")
        print()
    else:
        #Creating table
        print()
        print("Rescue Dogs")
        print("-----------")
        print(f"{'Name':<15} | {'Breed':<15} | {'Age':<5} | {'Weight'}")
        print("-" * 50)
        for dog in dog_roster:
            print(f"{dog.name:<15} | {dog.breed:<15} | {dog.age:<5} | {dog.weight}")
        print()

def findDog(dog_roster):
    search_name = input("Enter the name of the dog to search for: ")
    found = False

    for dog in dog_roster:
        if dog.name.lower() == search_name.lower():
            print()
            print("Dog Found!")
            print("-----------")
            print(f"{'Name':<15} | {'Breed':<15} | {'Age':<5} | {'Weight'}")
            print("-" * 50)
            print(f"{dog.name:<15} | {dog.breed:<15} | {dog.age:<5} | {dog.weight}")
            print()
            found = True
            break
    if not found:
        print(f"No dog named '{search_name}' was found in the roster.")
        print()



def main():
    dog_roster = []

    while True:
        menu()
        print()
        choice = input("Select a choice: ")

        # 1 - Add a dog
        if choice == '1':
            addDog(dog_roster)

        # 2 - View dogs
        elif choice == '2':
            viewDogs(dog_roster)

        # 3 - Find dogs
        elif choice == '3':
            findDog(dog_roster)

        # 4 - Exit
        elif choice == '4':
            print("Exiting program. Goodbye!")
            print()
            break

        # Invalid inputs
        else:
            print()
            print("Invalid input. Please enter 1, 2, 3, or 4.")
            print()

main()