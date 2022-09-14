#key - value şeklinde çalışır yani

# 16 -> bursayı temsil ediyor

sehirler = ['bursa','trabzon']
plakalar = [16,61]

print(plakalar[sehirler.index('bursa')]) #böylelikle 16 bilgisini alırız

plakalar = { 'bursa' : 16,'trabzon': 61 } # plakalar = { 'key' : 'value' }
print(plakalar['trabzon'])

plakalar['ankara'] = 6 #dictionary listelerinde bir değer eklemek istiyorsak böyle yapabiliriz
plakalar['bursa'] = 5 #böylelikle de 16 değerini 5 olarak değiştirdik
print(plakalar)

users = { #böyle yaparak daha profesyonel listeleme yapabiliriz
    'mertcanparlak' : {
        'age': 20,
        'roles': ['user'],
        'email': 'mert.166169@gmail.com',
        'address': 'bursa',
        'phone':'123456'
    },
    'huseyinparlak': {
        'age': 50,
        'roles': ['admin','user'],
        'email': 'hüseyin.166169@gmail.com',
        'address': 'bursa',
        'phone':'12354424456'
    }
}

print(users['huseyinparlak']['roles'][0]) #age bilgisi burda key'dir email diye koyarsak emaili de gösterir

dict1 = {
    'isim':'mesut', 
    'yas':32,  
    'lokasyon': {
    'yasadığı_yer':'Muş',
    'doğduğu_yer': 'Ağrı'}
    }
print(dict1)
print(dict1['yas']) #= print(dict1.get['yas'])
print(dict1['lokasyon']['yasadığı_yer'])

print(dict1.keys()) #Sözlük ifadesindeki Keyleri göösterir
print(dict1.values()) #Sözlük ifadesindeki valueleri gösterir
print(dict1.items()) #Sözlükteki her şeyi gösterir

d = {'sakarya':54,'adana':1,'ankara':2}
# Sözlük yapısı süslü parante içinde yazılır
# Elemanlar virgüllerle ayrılır.
# Her elemanda bir anahtar(key) ve bir değer(value) vardır

print(d['ankara'])
print(list(d.values())) #Liste biçiminde gösterdi

#Bir sözlüğe yeni bir anahtar ve değer ekleme#
d['ankara']=78
print(d)

#Soru 1
s={1:"aa","k":[1,2,3],2:{3:"klm"}}
#Klm değerini çağırın

print(s[2][3])


#Sözlükleri Döngülerde Kullanma#
for k in d.keys():
    print(k)

for k in d.values():
    print(k)

for k in d.items():
    print(k)

# Soru 2
#d sözlüğünde 1 değerine sahip anahtarı bulunuz

for k,v in d.items():
    if v==1:
        print(k)

#Soru 3
#d sözlüğünde değeri 10'dan büyük anahtarları göster

for k,v in d.items():
    if v>10:
        print(k)

#Soru 4
#d sözlüğünde anahtarların kaçının "A" ile başladığını bulunuz.

sayac = 0
for k in d.keys():
    if k[0]== "A":
        sayac=sayac+1
print(k)
        
