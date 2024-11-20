def ticket_price(age, day):
    if(age<18):
        day = day.lower()
        if(day=="wednesday" or day=="Wednesday"):
            print("Ticket Price is: 6$")
        else:
            print("Ticket Price is: 8$")

    elif(age>18 and age<100):
        if(day=="wednesday"):
            print("Ticket Price is: 10$")
        else:
            print("Ticket Price is: 12$")
    else:
        print("Wrong input. Try again")

age = int(input("Enter your age: \n"))
day = str(input("What is the day? \n"))

ticket_price(age, day)