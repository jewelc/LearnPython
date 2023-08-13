class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
    
        
    # def __str__(self):
    #     return f"total of {self.name} "

class Account(Person):
    def __init__(self, name, usd, eur, bdt, age=None):
        super().__init__(name, age)
        self.usd = usd
        self.eur = eur
        self.bdt = bdt


    def __str__(self):
        return f"Account: {self.name}, USD: {self.usd}, EUR: {self.eur}, BDT: {self.bdt}"


    def __add__(self, other):
        self.usd = self.usd + other.usd
        self.eur = self.eur + other.eur
        self.bdt = self.bdt + other.bdt
        return self

    


jewel = Account("jewel", 100, 150, 20000)
print(jewel)

champa = Account("champa", 250,0,25000)
print(champa)

total = jewel + champa
print(total)

# if __name__ == "__main__":
#     main()