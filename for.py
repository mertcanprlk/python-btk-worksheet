numbers = [1,2,3,4,5,6]

for a in numbers: #for (istediğimiz bir string değeri) in (sıralamayı istediğimiz listenin ismi)
    print(a) #print parantezinin içine 'hello' yazarsak 6 kere helloyu gösterir

names = ['ali','lale','ela']

for names in names:
    print(f'my name is {names}')
    print(names)

tuple = (1,2,3,4,5)
for t in tuple:
    print(t)

d = {'k1':1, 'k2':2,'k3': 3} #dictionary listelerinde sistem aşağıdaki gibi çalışır

for key,value in d.items():
    print(key,value)