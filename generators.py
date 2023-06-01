

#def cube():
#    for i in range(5):
#        yield i**3 burdaki yield bilginin belleğe kaydedilmemesini sağlıyor.
    
#for i in cube():
#    print(i)


generators = (i**3 for i in range(5))
print(generators)


for i in generators:
    print(i)