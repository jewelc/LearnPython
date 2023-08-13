def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     # return (name, house) #Tuple is immutable
#     return [name, house]

def get_student():
    # student= {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student
    name = input("Nme: ")
    house = input("House")
    return {"name": name, "house": house}



if __name__ == "__main__":
    main()