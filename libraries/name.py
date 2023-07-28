import sys

# try:
#     print("Hello, my name is", sys.argv[1])
# except:
#     print("Too few arguments")
# =======================

# if len(sys.argv) < 2:
#     print("Too few Arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else: 
#     print("Hello, my name is", sys.argv[1])

# # =========================
# if len(sys.argv) < 2:
#     print("Too few Arguments") #sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments") #sys.exit("Too many arguments")
# else
#     print("Hello, my name is", sys.argv[1])

# print("Hello, my name is", sys.argv[1])
# IndexError: list index out of range
# =======================
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is ", arg)