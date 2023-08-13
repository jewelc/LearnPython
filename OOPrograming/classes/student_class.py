class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Name is missing")
        if house not in ["Gryffindor", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} of {self.house} his/her patronus {self.patronus}"

    
def main():
    student = get_student()
    print(student)



def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
   
    return Student(name, house, patronus)



if __name__ == "__main__":
    main()