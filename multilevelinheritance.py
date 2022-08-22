class primary:
    standards = "1 to 5"
    def getGrade(self):
        print(f"your max to min grade is {self.garde}")

class Junior(primary):
    uniform ="black and white "
    time = "8 to 1 pm"
    def Timing(self):
        primary(f"the timing is {self.time} ")

class Hairstyle(Junior):
    length = "small"
    shoes="tidy"
    def Running(self):
        print("Running is not allowed")

p=primary()
j=Junior()
h = Hairstyle()
print(h.standards)

