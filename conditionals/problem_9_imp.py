def leap_check(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("It is a leap year")
    else:
        print("Not a leap year")

year = int(input("Enter year: \n"))

leap_check(year)