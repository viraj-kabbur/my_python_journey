def mode_of_Transport(distance):
    if (distance == 0):
        exit("Wrong input")
    if (distance < 3):
        print("Walk to the destination")
    elif (distance <= 15):
        print("Take a bike")
    elif (distance > 15):
        print("Take a car")

distance = float(input("Enter distance: \n"))

mode_of_Transport(distance)