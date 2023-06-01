# Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
# Ehliyen alma koşulu en az 18 ve eğitim durumu lise yada üniversite olmalıdır.
'''
isim=input("isminizi giriniz: ")
dt=input("doğum tarihinizi giriniz: ")
egitim=input("egitim durumunuzu giriniz: ")

yas =2020 - int(dt)

if yas>=18 and egitim=="üniversite" or egitim=="lise":
    print( "sayın ",isim, " ehliyet alabilirsiniz")
else:
    print("sayın ",isim, " ehliyet alamazsınız")
'''


#Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
# 0-24   => 0
# 25-44  => 1
# 45-54  => 2
# 55-69  => 3
# 70-84  => 4
# 85-100 => 5
'''
yazili1=int(input("1. yazılı sınav notunu giriniz: "))
yazili2=int(input("2. yazılı sınav notunu giriniz: "))
sozlu=int(input("sözlü  notunu giriniz: "))

ortalama= (yazili1+yazili2+sozlu)/3
mesaj=f"Not ortalamanız {ortalama} ortalamanıza karşılık gelen not bilgisi: "



if 0<=ortalama<=24:
    print(mesaj,0)
elif 25<=ortalama<=44:
    print(mesaj,1)
elif 45<=ortalama<=54:
    print(mesaj,2)
elif 55<=ortalama<=69:
    print(mesaj,3)
elif 70<=ortalama<=84:
    print(mesaj,4)
elif 85<=ortalama<=100:
    print(mesaj,5)
else:
    print("Bilinmeyen bir hata oluştu")
'''


#Trafiğe çıkış tarihi alınan bir aracın servis zamanı aşağıdaki bilgilere göre hesaplayınız
#1.Bakım => 1.Yıl
#2.Bakım => 2.Yıl
#3.Bakım => 3.Yıl

cikisT= int(input("Aracınızın trafiğe çıkış tarihini giriniz: "))

servis=2020-cikisT
print(f"Aracınızın trafiğe çıktığı tarihten bügüne {servis} yıl geçmiş ve {servis} kez bakıma girmiş bulunamkta")