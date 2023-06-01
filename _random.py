import random

#result = dir(random) içindeki parametreleri gösterir
#result = help(random) parametrelerin nasıl çalıştığını ve ne işe yaradıklarını söyler

result = random.random() #0.0 - 1.0 arasında random sayılar bulur
result = random.random() * 100
result = random.uniform(1,50) # aralığı sağlar ama yinee float bir değerdir.
result = int(random.uniform(1,50)) # bu şekilde int e çevrilebilir ama daha güzel yollarıda var.
result = random.randint(1,50) # sonucu direk intiger olarak verir.

names = ["selo", "can", "bus", "evrim", "hakki", "hasn", "mirac", "s2s","owo", "lul", "otto", "uwu"]
result = ( names[random.randint(0,len(names)-1)] ) #names listesi içinden random isim verir sondaki len listenin uzunluğunu ayarlar ve sürekli ayarlanmak zorunda kalmaz.

liste = list(range(0,11))
random.shuffle(liste) # sıralı olan listenin yerlerini karıştırır.

liste= range(100) 
result = random.sample(liste, 3) #liste içerisinden belirtilen sayı kadar eleman çeker ve o elemanları listenin içine koyar.


result = random.sample(names,3) #listenin içerisinde belitilen sayı kadar isim çeker yukarıdakinin aynısı ama string hali.

print(result)