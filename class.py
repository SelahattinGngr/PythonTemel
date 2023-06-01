#class
class Person:
    
    #class attiributes
    adresses = "no information "
    #constructor (yapıcı metod)
    def __init__(self,name,year):
        self.name=name
        self.year=year
        print("yapıcı metod çalıştı.")


        #methods

#object(instance)
p1=Person(name="Selo", year = 2001)
p2=Person(name="Busra", year = 1999)

#updating
p1.name="Selos"
p1.adresses="rize"
p2.adresses="Mugla"

#accsessing object attiributes
print(f'p1: name: {p1.name} year: {p1.year} adresses: {p1.adresses}')
print(f'p2: name: {p2.name} year: {p2.year} adresses: {p2.adresses}')




