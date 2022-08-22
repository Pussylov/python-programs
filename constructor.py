class Employee:
    def __init__(self,name,age,salary):
        self.name= name
        self.age = age
        self.salary=salary
        print("Employee is created!")
    def getDetails(self):
        print(f"Employee name is {self.name}")
        print(f"Employee age is {self.age}")
        print(f"Employee salary is {self.salary}")

karan = Employee("preet", 19, 500000)
karan.getDetails()