##Range Yapısı
from traceback import print_tb


lis = [1,2,3]

for item in lis:
    print(item)
#Bu şekilde yapmaktansa bu şekilde yapabilirsin#

for item in range(1,10):
    print(item)

#Hadi daha da kısaltarak böyle yapalım:
print(list(range(5,10)))

#Enumerate 
index = 0
bonjour = 'Salut'

for letter in bonjour:
    print(f'index {index} letter: {bonjour[index]}')
    index +=1
#Bu şekilde yapmaktansa bu şekilde yapabilirsin#
bonjour = 'Salut'

for letter in enumerate(bonjour):
    print(letter)

#Zip

list1 = [1,2,3,4]
list2 = ['a','b','c','d']

print(list(zip (list1,list2))) #Listeleri birbiriyle toplamak için zip yapısı kullanılır

for item in zip(list1,list2):
    print(item)