def pwd_checker(password):
    if (len(password) < 6):
        print("Password is Weak")
    elif (len(password) <= 10):
        print("Password is Medium")
    elif (len(password) > 10):
        print("Password is Strong")

password = str(input("Enter your password: "))

pwd_checker(password)