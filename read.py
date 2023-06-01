file = open("wuw.txt","w")

file= open("wuw.txt","a",encoding="utf-8")
file.write("Say My Name Moruq")
file.close()


file = open("wuw.txt","r",encoding="utf-8")

#for döngüsü
'''
for i in file:
    print(i,end="")
'''

#Read() fonksiyonu kıullanımı
'''
content = file.read()
print(content)

file.close()
'''
