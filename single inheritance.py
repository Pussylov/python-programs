class Student:
    standard="8th"
    def grade(self):
        print(f"this student studies in {self.standard}")

class Teacher(Student):
    subject = "physics"
    def Showdetail(self):
        print(f"the teacher teach {self.subject}")
a=Student()
a.grade()
b=Teacher()
b.Showdetail() 
     