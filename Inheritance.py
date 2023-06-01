class Person:
    def __init__(self,fname,lname):
        self.lname=lname
        self.fname=fname
        

    def Who_am_i(self):
        print("ım a person")

class Student(Person):
    def __init__(self, fname,lname, number):
        Person.__init__(self, fname, lname)
        self.number=number
    def Who_am_i(self):
        print("ım a student")

p1= Person("Selahattin","Güngör")
s1= Student("Busra","Kurekci",2416)
p1.Who_am_i()
s1.Who_am_i()

print(f'Person => name: {p1.fname} lastname: {p1.lname}')
print(f'Student => name: {s1.fname} lastname: {s1.lname} Number: {s1.number}')