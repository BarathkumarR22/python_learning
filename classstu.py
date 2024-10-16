class student:
    def __init__(self):
        self.name=""
        self.reg=""
    def display(self):
        print("Name:",self.name)
        print("RegNo:",self.reg)
st1=student()
st1.name= "Arun"
st1.reg="01"
st2=student()
st2.name= "Harini"
st2.reg="02"
st3=student()
st3.name= "Barath"
st3.reg="03"
st1.display()