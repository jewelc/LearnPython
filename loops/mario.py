# for i in range(3 ):
#     print("#")

def main():
    # print_column(3)
    # print_row(3)
    print_square(3)

    
def print_column(height):
    for i in range(height):
        print("#")
    # print("#\n" * height, end="")

          

def print_row(width):
    print("#" * width)


# Option One:
# =============
# def print_square(size):
#     # for each row in square
#     for i in range(size):
#         # for each brick in row
#         for j in range(size):
#             # print brick
#             print("#", end="")
#         print()

# Option two:
# ===============
# def print_square(size):
#     for i in range(size):
#         print("#" * size)


# Option Three;
# =============
def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()