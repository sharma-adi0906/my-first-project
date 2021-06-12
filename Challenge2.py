option = "w"
while True:
    print("please choose an option from the list below: ")
    print("1. Learn python")
    print("2. Learn Java")
    print("3. Go swimming")
    print("4. Have dinner")
    print("5. Go to bed")
    print("0. Exit")

    option = input("please enter a number\t")
    if option in "12345":
        print("You chose {}".format(option))
    elif option in "0":
        print("game over")
        break
