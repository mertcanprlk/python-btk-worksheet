from time import process_time_ns


numbers = [1, 10, 5, 16, 1, 2, 44]
letters = ['a','g','b','s', 'o']

val = min(numbers) #listedeki en küçük numara hangisi
val = max(letters) #listedeki en büyük harf hangisi
print(val)

val = numbers[3:5] #numbers listesindeki 3 ve 5 karakterleri arasındaki sayıları yazar
print(val)

numbers[4] = 40 #4 yerine 40 yazdırdık
print(numbers)

numbers.append(12) #listeye sayı ekledik
print(numbers)

numbers.insert(3, 2) #3. rakamı 2 ile değiştirdik
print(numbers)

numbers.pop() #son sayıyı parantez içine başka bir rakam gir1ilmediği müddetçe otomatik olarak siler 
print(numbers)

numbers.remove(44) #belirtilen sayıyı siler
print(numbers)

numbers.sort() #listeyi sayısal üstünlükle sıralar
print(numbers)

numbers.reverse() #listeyi tersine çevirir
print(numbers)

print(len(numbers)) #listedeki elemanları sayar
print(numbers)

print(numbers.count(44)) #listede belirtilen şeyden kaç tane var onu sayar
print(numbers) 

numbers.clear() #listedeki bütün elemanları siler
print(numbers)