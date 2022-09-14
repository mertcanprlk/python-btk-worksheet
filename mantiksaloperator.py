x=6
result = 5<x<20
print(result)

#Bu işlemi and, or ve not ifadeleriyle yapacağız bunlar mantıksal operatörlerdir

#and kullanımında true,true => true true,false =>false

result = x>20 and x>5
print(result)

hak = 5
devam = 'e'
result = (hak>0) and (devam == 'e') 
print(result)

#or kullanımında 1 tanesi true olması onu true yapmaya yeterlidir
result = (x>10) or (x % 3 == 0) #10dan büyük 11 var ama 3'e bölünmez bu durumda ikinci ifade yanlış olsa bile ilk ifade doğrudur o yüzden true sonucu çıkar
print(result)

#not kulllanımında true değilse false, false değilse true olur
result= not(x<5)
print(result)


