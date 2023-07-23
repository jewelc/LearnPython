# While loop:
# ============
# x = int(input("Insert a repeating number of Meow...! :"))
# while x != 0:
#     print("Meow")
#     x -= 1

# ==========================
#  For Loops

# for i in range(x):
#     print("Meow")

# Another way end="" is to avoid a last blank line
# print("Meow\n" * 3, end="")
# =========================
# CHECK IF INPUT IS GREATER THAN Zero
# while True:
#     x = int(input("What's number of Meow your want? :"))
#     if x > 0:
#         break

# for i in range(x):
#     print("Meow...")


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            # return n #optional way
            break
    return n

def meow(n):
    for i in range(n):
        print("Meow...")


main()