x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6
'''
#Kullanııdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
sayı1=input("1.sayı giriniz: ")
sayı2=input("2.sayı giriniz: ")

carpım=(int(sayı1)*int(sayı2))
toplam=(x+y+z)

print("işlem sonucu: ",(carpım-toplam))
'''
#y' nin x 'e kalansız bölümünü hesaplayınız.
#a= (y // x)
#print(a)


#(x,y,z) toplamının mod 3'ü nedir?
#toplam = (x+ y+ z)
#result= toplam % 3
#print(result)


#y' nin x. kuvvertini hesaplayınız.
#result=y ** x
#print(result)

#x, *y , z = numbers işlemine göre z'nin küpü kaçtır.
#numbers = 1, 5, 7, 10, 6
#x, *y ,z =numbers  #bu durumda x ilk elemanı z son elemanı y ise ortada kalan bütün elemanları alır.
#a=z*z*z
#print(a)


#x, *y, z = numbers işlemine göre y nin değeri toplamı kaçtır ?
x, *y, z = numbers
print(y)
a= (y[0])+(y[1])+(y[2])
print(a)