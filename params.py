def toplam(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b


def islem(f1 ,f2, f3, f4, islem_ne):
    if islem_ne == "toplama":
        print(f1(3,5))
    elif islem_ne == "çıkartma":
        print(f2(8,3))
    elif islem_ne == "çarpma":
        print(f3(4,5))
    elif islem_ne == "bölme":
        print(f4(12,3))
    else:
        print("Geçersiz değer")


islem(toplam, cikarma,carpma,bolme,"toplama" )
islem(toplam, cikarma,carpma,bolme,"çıkartma" )
islem(toplam, cikarma,carpma,bolme,"çarpma" )
islem(toplam, cikarma,carpma,bolme,"bölme" )
islem(toplam, cikarma,carpma,bolme,"toplamaaaaa" )

