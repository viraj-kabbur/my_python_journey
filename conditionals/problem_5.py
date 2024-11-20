def motivation_eng(weather):
    weather = weather.lower()
    if (weather == "sunny"):
        print("Go out for a walk")
    elif (weather == "rainy"):
        print("Read a Book")
    elif (weather == "snowy"):
        print("Build a Snowman")
    else:
        print("Wrong input. Try again")

weather = str(input("What's the weather like?\n"))

motivation_eng(weather)