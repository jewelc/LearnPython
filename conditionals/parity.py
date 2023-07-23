# x = int(input("What's x? "))

# if x % 2 == 0:
#     print(f"{x} is Even Number")
# else:
#     print(f"{x} is Odd Number")

# =============================

# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print(f"{x} is even number")
#     else:
#         print(f"{x} is odd number")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# main()
# =============================


# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print(f"{x} is even number")
#     else:
#         print(f"{x} is odd number")

# def is_even(n):
#     return  True if n % 2 == 0 else False


# main()

# ======================
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print(f"{x} is even number")
    else:
        print(f"{x} is odd number")

def is_even(n):
    return  n % 2 == 0


main()
