
while True:
    try:

        x = int(input("x : "))
        y = int(input("y : "))

        print(x/y)
    except Exception as ex:
        print("yanlış bir değer girdiniz.", ex)
    else:
        break
    finally:
        print("try except  bloğu durduruldu.")

