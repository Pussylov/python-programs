class primary:
    standards = "1 to 5"
    def getGrade(self):
        print(f"your max to min grade is {self.garde}")
    def Age(self):
        print("age is 87\n")

class Junior(primary):
    uniform ="black and white "
    time = "8 to 1 pm"
    def Timing(self):
        print(f"the timing is {self.time} ")
    def Age(self):
        super().Age()
        print("age is 15\n")


class Hairstyle(Junior):
    length = "small"
    shoes="tidy"
    def Running(self):
        print("Running is not allowed")

    def Age(self):
        super().Age()
        print("age is 56")

p=primary()
j=Junior()
h = Hairstyle()
h.Age()


