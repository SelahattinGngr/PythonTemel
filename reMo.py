import re
# re : Bir metni düzenlemek yada alt parçalarını elde etmek için kullanılır. mesela girilen bir değerin mail olup olmadığını anlamak bu formata uygun olup olmadığını kontrol etmek için kullanılır.


str = "Python eğitim kursu : Python programlama rehberiniz / 40 saat"


result= re.findall("Python",str) #içinde belirlenen değerden kaç tane olduğunu bulur ve len komutu ile sayıları belirlenir.
result=len(result)

result= re.split("40",str) # metni belirlenen yerden böler 

result= re.sub(" ", " anan ", str) #sub komutuherhangi bir metin içerisindeki bir kelimeyi istdiğimiz kelime yada alfanumerik değerle değişmemizi sağlar.
result= re.sub("\s", " anan ", str) #üstteki sub in aynısıdır ters \s boşluk anlamına geliyore.


result= re.search("programlama", str) #search komutu metin içerisinde istenilen kelimenin tam konumunu verir yalnız sadece ilk çıkan kelimenin adresini verir.
result= result.span() #span kodu ise search parametresinin içinden adresi olan bilgiyi çekmemizi sağladı.

print(result)


