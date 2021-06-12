number = "9,223;256:485 854;485;485"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
print(separators)

