# value types -> string,number
x = 5
y = 6

x = y 

y = 10 

print(x,y) #bu durumda x'e y'nin eski değeri yazılır

#reference types -> list 
a = ['a','e','c']
b = ['a','b','c']

a = b

b[0] = "d"
print(a, b)