
website = "http://www.sadikturan.com"
course   = "Python Kursu : Baştan Sona Python Programlama Rehberiniz ( 40 saat)"
KarakteS = len(course)
w=website[7:10]     #belli aralaığı almak için kullanılır
c=website[-3:]      #sondan 3 elemanı almak için kullanılır
ilk15=course[:15]   #ilk 15 elemanı almak için kullanılır
son15=course[-15:]  #sondan 15 elemanı almak için kullanılır
ters=course[::]   #tüm elemanları terten almak için kullanılır
print("course dizisinde bulunan karakter sayısı: ",KarakteS)
print(w)
print(c)
print(ilk15)
print(son15)
print(ters)
