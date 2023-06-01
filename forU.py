sayilar = [1,3,5,7,9,12,19,21]

#1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?
#2- Sayilar listesindeki sayıların toplamı kaçtır ?
#3- Sayilar listesindeki tek sayıların karesini alınız.

#1-   for n in sayilar:
#        if n % 3==0:
#          print(n)


#2-
#toplam= 0
#for sayi in sayilar:
#    toplam = toplam + sayi
#print(toplam)


#3-  for n in sayilar:
#       if n % 2 != 0:
#           print(n**2)


sehirler = ['kocaeli' ,'istanbul','ankara','izmir','rize']

# 4- şehirlerden hangileri en fazla 5 karakterlidir ?

#4-   for n in sehirler:
#        if len(n)<=5:
#            print(n)


urunler =[
    {"name":"samsung S6", "price": "3000"},
    {"name":"samsung S7", "price": "4000"},
    {"name":"samsung S8", "price": "5000"},
    {"name":"samsung S9", "price": "6000"},
    {"name":"samsung S10", "price": "7000"},
]
 

 # 5- Ürünlerin fiyatları toplamı nedir ?
 # 6- Ürünlerin fiyatı en fazla 5000 olan ürünleri gösteriniz ?


#5-    toplam=0
#    for urun in urunler:
#         fiyat = int(urun["price"]) 
#        toplam  += fiyat
#    print(toplam)

for urun in urunler:
   if int(urun["price"])<=5000:
       print(urun)

