import random
randomS=random.randint(1,10)
'''
y=int(input("kaç adet can sayısı istiyorsunuz: "))
sayi1=int(input("Bir sayı giriniz: "))

x=0

while x<y:
    if sayi1>randomS:
        print("aşşağıya")
        sayi1=int(input("yeni bir sayı giriniz: "))
        x+=1
    elif sayi1<randomS:
        print("yukarıya")
        sayi1=int(input("yeni bir sayı giriniz: "))
        x+=1
    elif sayi1==randomS:
        print("tebrikler doğru sayıyı buldunuz")
        break

print(f"Aradığınız random sayı: {randomS} ")
'''


can= int(input("İstediğiniz can sayısını giriniz: "))
hak = can
sayac=0
while hak>0:
    tahmin=int(input("Tahmin edeceğiniz sayıyı giriniz: "))
    sayac += 1
    
    if tahmin == randomS:
        print(f"Tebrikler sayıyı {sayac}. denemede buldunuz. puanınız : {100 - (100/can) * (sayac-1)}")
        break
    elif tahmin < randomS:
        print("Yukarıya")
    else :
        print("Aşşağıya")

    if hak==0:
        print(f"Bütün haklarınızı kullandınız random sayı : {randomS}")
