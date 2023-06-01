SeloHesap= {
    "isim" : "Selo",
    "HesapNo" : "123456789",
    "Bakiye" : 2000,
    "EkHesap" : 1000
}

EvrHesap= {
    "isim" : "Evrim",
    "HesapNo" : "23456789",
    "Bakiye" : 5000,
    "EkHesap" : 3000
}

def bankamatik(hesap, miktar):
    print(f"Merhaba {hesap['isim']}")

    if (hesap["Bakiye"] >= miktar):
        print("paranızı çekebilirsiniz.")
    
    else:
        toplam = hesap["Bakiye"] + hesap["EkHesap"]

        if toplam >= miktar:
            ekhesapKullanımı=input("Ek hesabınızı kullanmak istiyor musunuz (e/h)")

            if ekhesapKullanımı == "e":
                print("paranızı çekebilirsiniz")
            else: 
                print(f'{hesap["HesapNo"]} nolu hesabınızda {hesap["Bakiye"]} bakiye bulunmaktadır. ')
        else:
            print("üzgünüz  bakiye yetersiz.")

bankamatik(EvrHesap,6000)