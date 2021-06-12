import random

answer = random.randint(1, 10000)
guess = 0
print(answer)

while guess != answer:
    guess = int(input("please guess the number between 1 to 10000: "))
    if guess == answer:
        print("you got it")
        break
    else:
        if guess < answer:
            print("please guess higher")
        else:
            print("please guess lower")
    # guess = int(input())
    # if guess == answer:
    #     print("well, You guessed it right")
    # else:
    #     print("Sorry you have not guessed it correctly")
# guess = int(input("please guess a number between 1 and 10: "))
# print("You have guessed it correctly")
