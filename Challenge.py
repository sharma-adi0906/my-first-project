Name = input("What is your Name? ")
Age = int(input("How old are You?,{} ".format(Name)))

if 19 <= Age <= 30:
    print("You are allowed to go on Holiday")
elif Age>= 70:
    print("You are too old for this Holiday")
else:
    print("I'm sorry, you are not allowed {}".format(Name))