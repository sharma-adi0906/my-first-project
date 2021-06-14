import random

answer = random.randint(1, 10)
guess_number = 0
print(answer)
print("please guess the number between 1 to 10: ")



while guess_number != answer:

    guess_number = int(input())

    if guess_number == answer:
        print("you got it")
        break
    else:
        if guess_number < answer:
            print("please guess higher")
        else:
            print("please guess lower")

print(answer)