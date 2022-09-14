# Identity Operator: is 

x = y = [1,2]
z= [1,2]

print(x==y)
print(x==z)
print(x is y)
print(x is z) #Görünüşte x ve z eşit görünüyor ancak bu listeler belleğin ayrı adreslerine sahiptirler

x = [1,2]
y=[2,4]
print(x is y) #x ve y eşit mi? Eşit olmadığı için false gelecektir

del x[1] #x elemanındaki 1. değeri siler 
y[0] =1 #y listesindeki 0. elemanı 1 olarak değiştirdik
y.reverse
print(x==y)
print(x is y) #yine false gelecek -

#Membership operator: in
x= ['apple', 'melon']
print('melon' in x) #listede 'melon' adlı bir değer var mı?

name = 'mertcan'
print('a' in name)
print('a' not in name)