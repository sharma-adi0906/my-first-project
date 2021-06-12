available_exits = ["North" ,"East" ,"West" ,"South"]

choose_exit="none"
while choose_exit not in available_exits:
    choose_exit = input("Please enter the direction: ")
    if choose_exit.casefold() == "quit":
        print("you just Lost")
    break
print("You should glad that You're out.")