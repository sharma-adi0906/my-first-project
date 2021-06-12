Name = input("what is your name?")
age = int(input("how old are you, {0}?".format(Name)))

if age >= 18:
    print("You are eligible to vote")
else:
    print("come back in {} years to vote".format(18 - age))