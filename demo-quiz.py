class Question:
    def __init__(self, soru, siklar, cevap):
        self.soru = soru
        self.siklar = siklar
        self.cevap = cevap


    def checkcevap(self, cevap):
        return  self.cevap == cevap

q1=Question("En çok kullanılan programlama dili hangisidir", ["python","java", "c#","css"],"python")
q2=Question("En popüler kullanılan programlama dili hangisidir", ["c#","java","css","python"],"python")
q3=Question("En çok kazandıran programlama dili hangisidir", ["java","c#","css","python"],"python")

print(q1.checkcevap("python"))