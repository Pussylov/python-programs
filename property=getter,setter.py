class student:
    marks=80
    rechecking=5
    # totalmarks=85
    @property
    def totalamarks(self):
        return self.marks+self.rechecking
    @totalamarks.setter
    def totalamarks(self, value):
        self.rechecking=value-self.marks
e=student()
print(e.totalamarks)
e.totalamarks=90
print(e.rechecking)