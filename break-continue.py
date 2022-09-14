name = 'Ali At'

for letter in name:
    if letter == 'i':
        break #BREAK yazdığımız için ali isminde i harfine geldiğinde kod durur sadece 'al' kısmını yazar
    print(letter)

name = 'Sude Ak'

for letter in name:
    if letter == 'e':
        continue #Continue yazınca e harfini es geçer ama döngüyü çalıştırmaya devam eder
    print(letter)

x=0

while x< 5:
    if x == 2:
        break
    print(x)
    x+=1

# Örn
# 1-100 arası tek sayıların toplamı

x=1
result = 0

while x<= 100:
    x = x +1
    if x % 2 == 0:
        continue
    result += x
print(f'toplam: {result}')