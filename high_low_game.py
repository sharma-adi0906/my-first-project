h = int(input("please enter the higher number: "))  # higher number
l = int(input("please enter the lower number: "))  # lower number

print("")
guess = 0  # number of guesses
input("please think of a number between {} and {} in mind than press enter to continue...".format(l, h))

print("")3
g = 0  # guess
g = g + ((h + l) // 2)  # guess
p = "w"  # poll
while p != "c":
    print("")
    p = input(
        "my guess is {} if your guess is Higher -enter H, if Lower -enter L and enter C for Correct guess\t".format(
            g).casefold())
    if p == "h":
        l = g
        g = (g + ((h - l) // 2))

    elif p == "l":
        h = g
        g = (g - ((h - l) // 2))
    else:
        print("I've got it right in {} guesses".format(guess))
    guess += 1
