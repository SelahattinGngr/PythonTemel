'''
for n in range(80,101,10):
    print(n)
'''

'''
print(list(range(5,51,10)))
'''

'''
rakam=0
yazı ="Merhaba"

for yaz in yazı:
    print(f"sıra: {rakam} karşılık harf: {yaz}")
    rakam += 1
'''

'''
yazı ="Merhaba"

for index,yaz in enumerate(yazı):
    print(f"sıra: {index} karşılık harf: {yaz}")
'''

list1 = [1,2,3,4,5,6]
list2 = ["a","b","c","d","e","f"]

print(list(zip(list1,list2)))

