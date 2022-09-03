class number:
    def __init__(self, number):
        self.number  = number

    def __add__(self, number):
        return self.number + number.number
    def __mul__(self, number):
        return self.number *number.number
n1=number(20)
n2=number(30)
sum=n1+n2
mul=n1*n2
print(n1+n2)
print(mul)