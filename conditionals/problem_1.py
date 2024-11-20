def classify_age(age):
    if (age < 13):
        print("Kid")
    elif (age <= 19):
        print("Teenager")
    elif (age <= 59):
        print("Adult")
    elif (age > 59):
        print("Senior")
    else:
        print("Wrong input. Try again")


age = int(input("What is your age?\n"))

classify_age(age)


