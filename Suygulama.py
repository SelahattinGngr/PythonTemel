website = "htttp:www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1'webside' karkater dizisinin başındaki ve sonundaki boşlukları siliniz
#website=website.strip() sağdan silmek istersek rstrip  soldan silmek istersek lstrip kullanırız.

#2 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin
# sonuc = 'www.sadikturan.com'.strip('w.moc')

#3course karakter dizisinin tüm karakterlerini küçük harf yapın.
#course= course.lower()

#4'website' içinde kaç tane a karakteri vardır ? (count("a"))
#sonuc = website.count("a")

#5 'website' "www" ile başlayıp com ile bitiyor mu ?
#isFound = website.startswith("www")
#isFoundd = website.endswith("com")


#6  website  ifadesi içerisinde .com ifadesi var mı ?
#website = website.find(".com")




#8 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağına ve soluna * ekleyiniz.
result = "Contents".center(50, "*") 


#9 course karkater dizisindeki tüm boşluk karakterlerini "-" ile değiştirin.
result = course.replace(" ","-") 
print(result)

#10 "Hello World" dizisindeki "World" ifadesini "There" olarak değiştirin.
result ="Hello World"
wuw = result.replace("World","There")


#11 course karakter dizisini boşluk karkaterlerinden ayırın
result = course.split(" ")
print(result)