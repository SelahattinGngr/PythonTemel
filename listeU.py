araba=["Bmw","Mercedes","Opel","Mazda"]

#Liste kaç elemanlıdır
#print(len(araba))

#Listedeki ilk ve son eleman nedir
#print(araba[0])
#print(araba[3])


#mazda değerini Toyota ile değiştirin
#araba.remove("Mazda")      bu direk böyle de olabilio //araba[-1]="Toyota"// vay amk
#araba.append("Toyota")
#print(araba)

#Mercedes listenin bir elemanı mıdır
#deneme=araba.index("Mercedes") bu da şöyle olabiliyormuş // deneme = "Merdecedes" in araba// bele
#print(deneme)

#Listenin -2 indeksindeki değer nedir
#print(araba[-2])

#listenin ilk 3 elemanını alın
#print(araba[:3])

#Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin. 
#araba.pop(2)  bu şöyle de oluo  araba[-2:] = "Toyota","Renault"
#araba.pop(2)
#araba.append("Toyota")
#araba.append("Renault")
#print(araba)


#Listenin üzerine audi ve nissan değerlerini ekleyin.
#deneme=["Audi","Nissan",araba]
#print(deneme)

#listenin son elemanını silin
#del arabalar[-1]
#araba.pop(3)
#print(araba) 

#listedeki elemanları tersten yazdırınız.
#deneme=araba[::-1]
#araba.reverse()
#print(araba)

#aşağıdaki elemanları yeni bir liste için saklayınız
#studentA : Yiğit Bilgi 2010,(70,60,70)
#studentB : Sena Turan 1999,(80,80,70)
#studentC : Ahmet Turan 1998,(80,70,90)

studentA = ["Yiğit","Bilgi", 2010,[70,60,70]]
studentB = ["Sena","Turan", 1999,[80,80,70]]
studentC = ["Ahmet","Turan", 1998,[80,70,90]]

#Liste elemanlarını ekrana yazıdırınız

deneme =studentA[0]
print(f"{studentA[0]} {studentA[1]} {2021-studentA[2]} yaşında ve ortalamaya {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3} sahiptir.")