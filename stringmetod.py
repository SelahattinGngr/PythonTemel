message = "Hello There. My name is Selahattin Gungor"
#message = message.upper()                       Stringdeki bütün harflerin büyük olmasını sağlıyor
#message = message.lower()                       Stringdeki bütün harflerin büyük olmasını sağlıyor
#message = message.title()                       Stringdeki Kelimelerin baş harfinin büyük olmasını sağlıyor
#message = message.capitalize()                  Stringdeki sadece ilk harfin büyük olmasını sağlıyor
#message = message.strip()                       Stringin başındaki boşluk karakteri yok olur
#message = message.split()                       Stringi böler
#message = message.split(".")                    Aynı şekilde böler ama böyle yapılırsa nereden bölüneceğini seçerisz örnekteki gibi . dan böler
#message = "*" .join(message)                    Her karakterden sonra eklenmesini istediğimiz bir karakteri eklememizi sağlar
#index = message.find("Mertcan")                 String içerisinde istediğimiz elemanın kaçıncı sırada olduğunu gösterir
#isFound = message.startswith("H")               Stringin bu elemanla başlayıp başlamadığını sorgular
#isFound = message.endswith("r")                 Stringin bu elemanla mı bittiğini sorar sorgular
#message = message.replace("Mertcan","Cancan")   String içerisinde istediğimiz elemanın yerine istediğimiz elemanı koymamızı sağlar
#message = message.center(100)                   100 birimlik bir konteynır oluşturur ve ortasıa yerleştirir


print(message)