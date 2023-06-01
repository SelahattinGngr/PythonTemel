class Circle:
    pi=3.14

    #class object attributes
    def __init__(self,yaricap=1):
        self.yaricap=yaricap
    
    #methods
    def alanHesapla(self):
        return self.pi * (self.yaricap**2)

    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap

c1=Circle()
c2=Circle(5)

print(f' dairenin alanı: {c1.alanHesapla()} daireni çevresi: {c1.cevreHesapla}')
print(f' dairenin alanı: {c2.alanHesapla()} daireni çevresi: {c2.cevreHesapla}')
    