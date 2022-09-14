list = [1,2,3]

tuple = (1, 'sa', 5) #parantezi kullanmak opsiyonel

print(type(list))
print(type(tuple))

print(type(list[2])) #2. sayının tipini gösterir
print(type(tuple[0]))

ilist = ['ali','ela']
tuple = ('leyla','lale','leyla')
names = ('veli','aslı') + tuple #böylelikle listenin yanına tuple listesini koyabiliriz ancak iki liste aynı anda birleştirilemez bu yöntemle
print(names)

ilist[0] = 'ahmet'
# tuple[1] = 'aslı' #tuple'de elemanların kendilerini değiştiremezsin o yüzden bu kod çalışmaz

print(tuple.count('ayse')) #tuple'nin içerisinde ayse diye bir değer var mı onu sorguladık
print(tuple.index('leyla')) #ilk defa nerede kullandıysa oradaki indeks numarasını belirtir

print(ilist)
print(tuple)

