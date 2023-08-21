name = input("what's your name? ")

# file = open("names.txt", "a") #"w" always replace the old one
# file.write(f"{name}\n") #\n save the new input toa new line
# file.close()

# Improve this

with open("names.txt", "a") as f:
    f.write(f"{name}\n")