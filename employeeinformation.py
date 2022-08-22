class Programmer:
    company= " microsoft"
    def __init__(self,name,age,skill):
        self.name= name
        self.age = age 
        self.skill= skill
        print("Employee list is created")

    def getDetails(self):
        print(f"Employee name is{self.name} ")
        print(f"Employee age is{self.age} ")
        print(f"Employee skill is{self.skill} ")

a = Programmer(input("enter your name"), int(input("enter your age")), input("enter your skill"))

a.getDetails()