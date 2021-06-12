numbers = [1, 25, 32, 46]

for number in numbers:
    if number % 8 == 0:
        print("numbers are unacceptable")
        break
else:
    print("numbers are fine")
