#Girilen bir sayının 0 ile 100 arasında olup olmadığını doğrulayınız.
#sayi1 = int(input("sayı giriniz: "))
#deneme= 0<sayi1<100
#print("girilen değer 0 ile 100 arasındadır: ",deneme)



#Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
#sayi1 = int(input("sayı giriniz: "))
#deneme= (sayi1%2==0) and (sayi1>=0)
#print("Girilen sayı pozitif çift sayıdır: ",deneme)



#Email veya parola bilgileri ile giriş kontrolü yapınız.
#email ="selahattin_gungor53@hotmail.com"
#parola ="deneme123"
#Zemail = input("email giriniz: ")
#Zparola = input("parola giriniz: ")
#Zemail=Zemail.strip()
#Zparola=Zparola.strip()
#kontrol = (Zemail==email) and (Zparola==parola)
#print("girilen parola ve email eşleşiyor: ", kontrol)



#Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
#sayi1 = int(input("1.sayı giriniz: "))
#sayi2 = int(input("2.sayı giriniz: "))
#sayi3 = int(input("3.sayı giriniz: "))
#deneme=[sayi1,sayi2,sayi3]
#deneme.sort()
#print(deneme)

#Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
#a) Ortalama 50 olsa bile final notu en az 50 olmalıdır
#b) Finalden 70 alındığında ortalama önemli olmasın.
'''
vize1 = int(input("1. vize notunuzu giriniz: "))
vize2 = int(input("2. vize notunuzu giriniz: "))
final = int(input("final notunuzu giriniz: "))

hesaplama=(vize1+vize2)/2 * 0.6 + (final*0.4)
print("ortalmanız: ",hesaplama)

if final>=70 or hesaplama>=50 and final>=50:
    print("geçti")
else:
    print("kaldı")
'''


# Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# Formül: (Kilo / boy uzunluğunun karesi)
# Aşağıdaki tabloya göre kişi hangi gruba girmektedir 
# 0-18.4     => zayıf
# 18.5-24.9  => normal
# 25.0-29.9  => fazla kilolu
# 30.0-34.9  => şişman (obez)
'''
isim = input("İsminizi Giriniz: ")
kilo = float(input("Kilonuzu giriniz : "))
boy = float(input("Boyunuzu giriniz (metre cinsinden): "))

indeks= kilo/(boy**2)
print("kilo endeksiniz: ",indeks)

if  indeks<=18.4:
     print("Zayıfsınız.")
elif 18.5<=indeks<=24.9:
    print("Normalsiniz.")
elif 25.0<=indeks<=29.9:
    print("Normalsiniz.")
elif 30.0<=indeks:
    print("Obezsiniz. ")
else:
    print("Bilinmeen bir hata oluştu.")
'''