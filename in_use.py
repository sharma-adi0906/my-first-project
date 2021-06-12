Parrot = "Norwegian Blue"

Letter = input("What is the letter you want to check? ")

if Letter in Parrot:
    print("{} is in {}".format(Letter,Parrot))
else:
    print("I dont need that letter")


Activity = input("What would you like to do today? ")
if "Cinema" not in Activity.casefold():
    print("But I would like to go to Cinema")
else:
    print("Let's go")