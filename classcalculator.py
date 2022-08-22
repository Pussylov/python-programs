class Calculator:
    def __init__(self,num):
        self.num   = num
    def SquareRoot(self):
        print(f"the value of {self.num} is {self.num**0.5} ")
    def SquareCube(self):
        print(f"the value of {self.num} is {self.num**3} ")
        
a = Calculator(16)
a.SquareRoot() 
a.SquareCube()
