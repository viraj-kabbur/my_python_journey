def pet_food_recc(species, age):
    species = species.lower()

    if (species == "dog" and age < 2):
        print("Puppy food is reccommended")
    elif (species == "dog" and (age > 2 and age<25)):
        print("Pedigri is reccommended")

    elif (species == "cat" and age < 2):
        print("Junior cat food is reccommended")
    elif (species == "cat" and (age > 2 and age<25)):
        print("Senior cat food is reccommended")
    else:
        exit("Wrong input")

species = str(input("Enter species: \n"))
age = float(input("Enter age: \n"))

pet_food_recc(species, age)