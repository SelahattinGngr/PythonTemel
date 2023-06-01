'''
ogrenciler = {
        '120:{
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125':{
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128':{
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
}
'''



ogrencinum=input("Öğrenci numarası giriniz: ")
ogrenciad=input("Öğrenci ismini giriniz: ")
ogrencisoyad=input("Öğrenci soyismini giriniz: ")
ogrencitel=input("Öğrenci telefon numarasını giriniz: ")

ogrenci={
    ogrencinum:{
        "isim" :ogrenciad,
        "soyad":ogrencisoyad,
        "telefon":ogrencitel
    }
}
print(ogrenci)

'''
ogrenciler = {
        '120':{
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125':{
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128':{
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
}
'''
#numara=input("Öğrenci numarası giriniz: ")
#(ogrenciler[numara])
