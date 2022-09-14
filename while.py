# numbers = [1,2,3,4,5,6]

# for a in numbers: #for (istediğimiz bir string değeri) in (sıralamayı istediğimiz listenin ismi)
#     print(a) #print parantezinin içine 'hello' yazarsak 6 kere helloyu gösterir

##Diyelim ki böyle bir liste elimizde yoksa ancak yinede sıralı ifadeleri yazdırmak istiyorsak while kullanmalıyız.

#1-100 e kadar
x =0 

while x<=100: 
    print(x) #eğer x = X+1 yazmazsak devamlı 0 yazmaya devam eder bunu durdurmak için x = x+1 ifadesini koyduk
    x = x +1
print('bitti')

name = '' 
while not name: #not name true'yi ifade eder çünkü name boşluktur
    name = input('isminizi giriniz: ')
print(f'merhaba, {name}')

#while değeri işlem true ifadesi döndürdükçe çalışır

