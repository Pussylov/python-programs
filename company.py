class Employee:
    company = "google"

Preet = Employee()
singha = Employee() 
print(Preet.company)
print(singha.company)
Employee.company = "microsoft"
print(Preet.company)
print(singha.company)