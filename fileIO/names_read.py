# with open("names.txt", "r") as f:
#     persons = f.readlines()

# for person in sorted(persons):
#     print(f"hello, {person}",end="")
    
# ==================================
with open("names.txt", "r") as f:
    for person in sorted(f):
        # print(f"helo, {person}", end="")
        print(f"hello, {person.rstrip()}")
# ==================
# names = []

# with open("names.txt" , "r") as f:
#     for line in f:
#         names.append(line.strip())

# for name in names:
#     print(f"hello, {name}")

# =====================
