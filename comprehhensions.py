for x in range (10):
    print(x)
#Bunu yapmak yerine bunu yapabiliriz:

number = [x for x in range(10)]
print(number)

number = [x/2 for x in range(10)]
print(number)

numbers = [x*x for x in range(10) if x%3 ==0]
print(numbers)

myString = 'Hi'
myList = []

for letter in myString:
    myList.append (letter)
print(myList)

myList = [letter for letter in myString]
print(myList)

years = [1983,1965,1989,1999,2010]
ages = [2022-year for year in years]
print(ages)

resulte = [x if x%2==0 else 'tek' for x in range(1,10)]
print(resulte)

numbers = [(x,y) for x in range(3) for y in range (3)]