sayi = int(input("sayi giriniz: "))
asalmi = True
 

if sayi == 1:
    print("1 asal sayı değildir")

for i in range(2, sayi):
    if sayi % i == 0:
        asalmi=False
        break

if asalmi==True:
    print(f"{sayi} bir asal sayıdır.")
else :
    print(f"{sayi} bir asal sayı değildir.")