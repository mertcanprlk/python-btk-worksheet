#Method
lis = [1,2,3]
lis.append(4) #4ü sona ekler
lis.pop() #Sona eklenen 4'ü siler

print(type(lis))
print(lis)

#Fonksiyon
def sayhi():
    print('hi')
sayhi()

def besbastir():
    print(5)
besbastir()

def sayhello(name = 'user'):
    print('hello ' + name)
sayhello('ada')
sayhello()

def sayhello(name = 'user'):
    return 'hello ' + name ##Print yerine artık returnu kullanıyoruz aynı işlevi görüyor
msg = sayhello('Ali')
print(msg)

def besyazdir(sayi):
    return sayi
k = besyazdir(5)
print(k)

def total(num1, num2):
    return num1 + num2

resul = total(10,25)
print(resul)

def hangisibüyük(a,b): #eğer ifli ifadeler yoksa ve iki return yazıldıysa ilk return esas alınır
    if a>b:
        return a
    if b>a:
        return b

k=hangisibüyük(10,4)
print(k)

def yasHesapla(dogumYili):
    return 2022 - dogumYili

ageCinar = yasHesapla(2015)
ageAli = yasHesapla(2005)
ageAda = yasHesapla(2010)

print(ageAda,ageAli,ageCinar)

def emekliligekaçyilkaldi(dogumyili,isim):
    '''
    DOCSTRİNG: Doğum yılınıza göre emekliliğinize kaç yıl kaldı 
    INPUT: Doğum yılı
    OUTPUT: Hesaplanan yıl bilgisi
    '''
    yas = yasHesapla(dogumyili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'emekliliğine {emeklilik} yıl kaldı')
    else:
        print('zaten emekli oldunuz')

emekliligekaçyilkaldi(1985, 'ada')
emekliligekaçyilkaldi(1999, 'ali')
emekliligekaçyilkaldi(1909, 'lale')

# print(help(emekliligekaçyilkaldi)) #Bu komut çalışmamaktadır