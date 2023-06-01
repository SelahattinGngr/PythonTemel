liste = ["1","2","5a","10b","abc","10","50"]
# 1: Liste elemanları içindeki sayısal değerleri bulunuz.
'''
def chek_list(lst):
    import re
    for i in lst:
        if not re.search("[a-z]",i):
            print(i)

chek_list(liste)

*********bu işlem böyle de yapılabilir**********

for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue
'''

#2: kullanıcı 'q' değeri girmedikçe aldığınız her inputun sayı değeri olduğundan emn olun aksi halde hata mesajı yazın
'''
sayılar = []
while True:
    import re
    a = input("Sayı giriniz: ")
 
    if a=="q":
        break
    elif  re.search("[a-z]",a):
        raise Exception("Değer harf içermemelidir.")
    elif  re.search("[A-Z]",a):
        raise Exception("Değer büyük harf  içermelidir.")
    elif  re.search("\s",a):
        raise Exception("Değer boşluk içermemelidir.")
    else:
        sayılar.append(a)

print(sayılar)
*******diğer şekli*********
bu şekil üstteekinden daha başarılı çünkü hocanın yaptığı amk

while True:
    sayi =input("sayı giriniz: ")
    if sayi=="q":
        break

    try:
        result = float(sayi)
        print("girdiğiniz sayı: ",sayi)
    except ValueError:
        print("Geçersiz sayı")
        continue
'''



#3: Girilen parola içindeki türkçe karakter hatasi veriniz
'''
def check_pass(psw):
    import re

    if  re.search("[üğşçöıİÜĞŞÇÖ]",psw):
        raise Exception("parola türkçe karakter içeremez.")
    else:
        print("parola seçiminiz başarılı olmuştur")

parola = input("parola giriniz: ")
try:
    check_pass(parola)
except Exception as ex:
    print(ex)


    *******diğer şekli*********

turkce_karakterler="üğşçöıİÜĞŞÇÖ"
parola = input("parola: ")
for i in parola:
    if i in turkce_karakterler:
        raise TypeError("parola türkçe karakter içeremez")
    else:
        pass
print("parola geçerli")
'''

#4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı verin.



    


