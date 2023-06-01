'''
def decorator(func):
    def deneme(name):
        print("fonksiyondan önceki işlem")
        func(name)
        print("fonksiyondan sonraki işlem")
    return deneme
'''

'''
def sayHello():
    print("hello")

def sayGreeeting():
    print("greeting")

sayGreeeting = decorator(sayGreeeting)
sayGreeeting()
'''

'''
import math
import time

def usalma(a,b):
    startT = time.time()
    time.sleep(1)
    print(math.pow(a,b))

    finisH = time.time()
    print( "İşlem " + str(finisH-startT) + "saniye sürdü")


def faktöriyel(num):
    print(math.factorial(num))


usalma(2,3)
'''



import math
import time

def calculate_time(func):
    def inner(*args , **kwargs):
        startT = time.time()
        time.sleep(1)
        func(*args , **kwargs)
        finisH = time.time()
        print( "İşlem " + str(finisH-startT) + "saniye sürdü")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))



def faktöriyel(num):
    print(math.factorial(num))

usalma(2,3)
