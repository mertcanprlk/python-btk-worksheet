#Fonksiyonların birbirleriyle olan ilişkisi
def hangisibüyük(a,b): #eğer ifli ifadeler yoksa ve iki return yazıldıysa ilk return esas alınır
    if a>b:
        return a
    if b>a:
        return b

k=hangisibüyük(1,4)
print(k)

def metin_yazdir(a,b):
    buyuk_sayi = hangisibüyük(1,4)
    sablonmetin = (f'{hangisibüyük} daha büyük sayidir'.format(buyuk_sayi))
    print(sablonmetin)

#Fonksiyonlar ile Referans atamaları
def changeName(n):
    n='ada'

name = 'ali'
changeName(name)
print(name)

def sehirler(n):
    n[0] = 'izmir'

sehirler = ['Muş','Van']
n = sehirler
n[0] = 'İzmir'
print(sehirler)

def add(a,b):
    return sum((a,b)) #Burada a değişkeni ve b değişkenini topladık sum komutu toplamaya yarar
print(add(10,20))

def add(*params): #Eğer çok fazla değişken varsa bu değişkenleri tek tek yazmak yerine *.... (başına yıldız sonrasında herhangi bir string değer) koyabiliriz tek yıldız koyma nedenimiz bir tuple listesi olduğunu göstermemiz içindi
    print(type(params)) 
    return sum((params))
print(add(10,50,70))

def displayUser(**args): #Dictionary bir değer girildiğini göstermek için iki yıldız koyduk
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser (name='Ali', age=5,city = 'muş')
displayUser (name='Ada', age=15,city = 'ağrı',phone = '123456798')
displayUser (name='Ata', age=25,city = 'van', phone = '123456123', email='ata@gmail.com')

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50, key1='value 1', key2 = 'value2')










