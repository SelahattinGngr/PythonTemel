# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# Kullanımı : open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.,

# 'w': (Write) yazma modu. Dosyayı konumda oluşturur.
# 'a': (Append) ekleme. Dosya konumunda yoksa oluşturur.
# 'x': (Create) oluşturma. Dosya zaten varsa hata verir.
# 'r': (Read) okuma. varsayılan. dosya konumunda yoksa hata verir.

#file = open("aaa.txt","w")
#file.close()

#file = open("C:/Users/User/Desktop/deneme.txt","w")
#file.close()

#file = open("aaa.txt","w",encoding="utf-8")
#file.write("Selo")
#file.close()

#file = open("aaa.txt","a")
#file.write("\noluyomu lan")
#file.close()