# ValueError once use inputs float/letters
# ================================= try ===> except
# Option One:
# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print(f"Input is not an Integer")

# Option two:
# ============
# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print(f"Input is not an Integer")
# else:
#     print(f"x is {x}")


# Option Three: More accurate way to looping untill user gives correct input
# ==============(Never ending loop)
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print(f"Input is not an Integer")
#     else:
#         print(f"x is {x}")


# Correct way one
# =============
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print(f"Input is not an Integer")
#     else:
#         break

# print(f"x is {x}")


# Correct way tow
# =============


# while True:
#     try:
#         x = int(input("What's x? "))
#         break
#     except ValueError:
#         print(f"Input is not an Integer")

# print(f"x is {x}")


# Defining with a function:
# =============
def main():
    x = get_integer("What's your number is? ")
    print(f"x is {x}")


    
# def get_integer():
#     while True:
#         try:
#             x = int(input("What's x? "))
#             break
#         except ValueError:
#             print(f"Input is not an Integer")
#     return x


# more shorter
# ================
# def get_integer():
#     while True:
#         try:
#             # x = int(input("What's x? "))
#             # return x
#             return int(input("What's x? ")) # shorter of previous tow lines
#         except ValueError:
#             print(f"Input is not an Integer")
#             # pass # use pass when you do not want to show error to user

# ====================
# =================
def get_integer(prompt):
    while True:
        try:
            # x = int(input("What's x? "))
            # return x
            return int(input(prompt)) # shorter of previous tow lines
        except ValueError:
            print(f"Input is not an Integer")
            # pass # use pass when you do not want to show error to user

main()