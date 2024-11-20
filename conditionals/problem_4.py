def ripeness_check(color):
    color = color.lower()
    if (color == "green"):
        print("Your fruit is Unripe")
    elif (color == "yellow"):
        print("Your fruit is Ripe")
    elif (color == "brown"):
        print("Your fruit is Overripe")
    else:
        print("Unknown Color. Please try again")

color = str(input("Enter color of your fruit: "))

ripeness_check(color)
