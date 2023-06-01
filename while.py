sayilar =[1,3,5,7,9,12,19,21]

#1: sayilar listesini while ile ekrana yazıdırın.
#2 Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
#3: 1-100 arasındaki sayıları azalan şeklinde yazın
#4: kullanıcıdan alacağımız 5 sayıyı ekranda sıralı bir şekilde yazdırın 
#5: Kullanııdan alacağınız sınırsız ürün bilgisini urunler listesi  içinde saklayınız.
# ** ürün sayısını kullanıcıya sorun 
# ** dictionary listesi yapısı (name, price) şeklinde olsun
# ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin

#1-  i=0
#    while (i < len(sayilar)):
#       print(sayilar[i])
#       i += 1
'''
2-
sayi1 = int(input("sayı giriniz: "))
sayi2 = int(input("2.sayıyı giriniz: "))
i = sayi1
while i < sayi2:
    i += 1
    if i % 2 != 0:
         print(i)
'''


#3-  i = 100
#    while i > 0:
#        print(i)
#        i -= 1

'''
4-
sayi1 = int(input("1.Sayi giriniz: "))
sayi2 = int(input("2.Sayi giriniz: "))
sayi3 = int(input("3.Sayi giriniz: "))
sayi4 = int(input("4.Sayi giriniz: "))
sayi5 = int(input("5.Sayi giriniz: "))

liste =[sayi1,sayi2,sayi3,sayi4,sayi5]
liste.sort()

i = 0
while i < len(liste):
    print(liste[i])
    i += 1 

#farklı bir metod
numbers =[]

i = 0
while i<5:
    sayi=int(input("sayi giriniz: "))
    numbers.append(sayi)
    i+=1

for n in numbers:
    print(n)
'''
urunler = []
adet= int(input("Kaç adet ürün eklemek istiyorsunuz: "))
i=0
while i<adet:
   name = input("eklemek istediğiniz ürünün ismi: ")
   price = input("ürünün fiyatı: ")


   urunler.append({
       "name": name,
       "price": price
   })
   i += 1

   for urun in urunler:
       print(f"ürünün ismi: {urun['name']} ürünün fiyatı: {urun['price']}")
       