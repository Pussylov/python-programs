class Manager:
    company="Preet's technology pvt ltd"
    def credit(self): 
        print(f"salary working in {self.company} is {self.salary}")


sandeep = Manager()
sandeep.salary= 400000
sandeep.credit() # Manager.credit(sandeep)