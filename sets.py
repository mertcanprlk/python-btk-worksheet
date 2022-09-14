vegetables = { 'cucumbers', 'tomatoes','patatoes'}

# print(vegetables[1]) #indekselenemz

for x in vegetables: #listedik her bir elemanı bu şekilde ayrı ayrı indekseleyebiliriz
    print(x) #burada demek istediğimiz sebzeler içerisindeki her ifadeyi dön dolaş bir kere yaz

vegetables.add('lettuce')
vegetables.update(['courgette', 'lemon']) #.add yerine bunu da yapabiliriz. Listede zaten var olan şeyleri tekrardan ekleyemiyoruz
print(vegetables)

myList = [1,2,3,4,4,6,8,5] 
print(set(myList)) #böylelikle listemizi düzenleyebilir ve tekrar eden ifadeleri silebiliriz

vegetables.remove('cucumbers') 
vegetables.discard('cucumbers') #bu üç kodda kaldırılmak istenilen şeyi listenen kaldırır
vegetables.pop()

vegetables.clear() #listedeki her şeyi siler

print(vegetables)
