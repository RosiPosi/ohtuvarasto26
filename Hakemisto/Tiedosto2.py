x = "y"
list = []
while x == "y":
    food = input("Give a tasty dinner idea: ")
    list.append(food)
    print(f"{food} added to the menu!")
    print(f"Menu: {list}")
    x = input("Would you like to add more? (y/n): ")
    if x != "y" and x != "n":
        print("Reply not recognized.")
print("Thank you for your input!")
