def grade_calc(score):
    if (score < 60):
        print("Your grade is: F")
    elif (score < 70):
        print("Your grade is: D")
    elif (score < 80):
        print("Your grade is: C")
    elif (score < 90):
        print("Your grade is: B")
    elif (score <= 100):
        print("Your grade is: A")
    else:
        print("Wrong score give. Try again")

score = int(input("Enter your score:\n"))

grade_calc(score)