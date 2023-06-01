#Gönderilen bir kelimeyi belirtilen sayı kadar tekrar ettiriniz.
'''
def kelime(yazı,adet):
    print(yazı * adet)

kelime("vayamk\n",5)
'''

#fonksiyona atanan sınırsız parametreyi listeye dönüştürün
'''
def liste(*params):
    list1=[]

    for param in params:
        list1.append(param)
    return list1

yazdır = liste(2,13,54,654,32,1)

print(yazdır)
'''

#Girilen 2 sayı arasında asal sayıları gösteriniz
'''
def asalsayi(sayi1,sayi2):
    for i in range(sayi1,sayi2):
        if i>1:
            for n in range(2,i):
                if (i % n == 0):
                    break
            else:
                print(i)

                
sayi1 = int(input("1. sayıyı giriniz: "))
sayi2 = int(input("2. sayıyı giriniz: "))
asalsayi(sayi1,sayi2)
'''

#Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.

def tambolen(sayi):
    liste= []

    for i in range(2, sayi):
        if sayi % i == 0:
            liste.append(i)

    return tambolen

print(tambolen(12))


