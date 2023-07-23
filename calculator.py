# x = int(input("What is your x? "))
# y = int(input("what is your y? "))

# print(x + y)

# x = float(input("What is your x? "))
# y = float(input("what is your y? "))

# z = round(x + y,1) 
# a = round(x / y, 2)

# thousand sperator
# print(f"Answer: {a:,}")

# RETURN KEY WORD USES

def main():
    x = int(input("what's x?"))
    print(f"x squared is {square(x)}")

def square(n):
    return pow(n,2)

main()