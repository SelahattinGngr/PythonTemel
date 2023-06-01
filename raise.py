'''
x = 10 

if x > 5:
    raise Exception("x 5 den büyük olamaz.")
'''


'''
def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("parola en az 7 karakter olmalıdır.")
    elif not re.search("[a-z]",psw):
        raise Exception("parola küçük harf içermelidir.")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola büyük harf içermelidir.")
    elif not re.search("[1-9]",psw):
        raise Exception("parola rakam içermelidir.")
    elif not re.search("[$_@]",psw):
        raise Exception("parola alpha numric karakter içermelidir.")
    elif  re.search("\s",psw):
        raise Exception("parola boşluk içermemelidir.")
    else:
        print("parola seçiminiz başarılı olmuştur")

password="1234567aB_"

try:
    check_password(password)
except Exception as ex:
    print(ex)
finally:
    print("try except kod bloğu tamamlandı")
'''

class Person :
    def __init__(self, name, age):
        if len(name) > 10:
            raise Exception("name alanı fazla karakter içeriyor.")
        else:
            self.name = name

p = Person("Heisenberrggg",20)



