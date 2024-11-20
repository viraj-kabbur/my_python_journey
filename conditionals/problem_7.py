def coffee_check(size, extra_shot):
    size = size.lower()
    extra_shot = extra_shot.lower()

    if (size == "small"):
        if (extra_shot == "yes"):
            print(f"Your order is a {size} Coffee with an extra shot of espresso")
        else:
            print("Your order is a Small Coffee")

    elif (size == "medium"):
        if (extra_shot == "yes"):
            print(f"Your order is a {size} Coffee with an extra shot of espresso")
        else:
            print(f"Your order is a {size} Coffee")

    elif (size == "large"):
        if (extra_shot == "yes"):
            print(f"Your order is a {size} Coffee with an extra shot of espresso")
        else:
            print(f"Your order is a {size} Coffee")
    else:
        exit("Wrong input. Try again")

size = str(input("Enter size of coffee: "))
extra_shot = str(input("Do you want an extra shot of espresso?"))

coffee_check(size, extra_shot)