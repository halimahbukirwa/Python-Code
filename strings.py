#strings
'hello'

"World"

'I am learnimg how to slice'

"It's so much fun"

"Hello World One"
"Hello World Two"

print('Hello World One')
print('Helo World Two')

print('Hello \nWorld')

print('hello \tWorld')

len('Hello')

len("I am")

mystring = "Hello World"

print(mystring[1])

print(mystring[-1])

print(mystring[6])

#SLICING

mystring

mystring = 'abcdefghijk'


print(mystring)

print(mystring[0:5])

print(mystring[3:])

print(mystring[:4])
print(mystring[3:8])

#STEP SIZE

print(mystring[::])

print(mystring[::2])

print(mystring[::3])

print(mystring[0:7:2])
print(mystring[::-1])

#IMMUTABILITY

name = 'Sam'

#name[0] = 'P'

Last_Letters = name[1:]

Last_Letters

'P' + Last_Letters

x = 'Hello World'

x = x + ' it is beautiful outside'
print(x)

letter = 'z'

print(letter*10)

#STRING METHODS

x = 'Hello World'

x.upper()

print(x)

x.lower()

print(x)

x.split()

y = 'Hello It is a beautiful day today'

y.split()

y.split('a')

#STRING FORMARTING

print('This is a string {}'.format('INSERTED'))

print('This is a {2} {0} {1}'.format(('brown'),('fox'),('quick')))

print('This is a {q} {b} {f}'.format(b='brown',f='fox',q='quick'))

# Float Formating with a .format method {value:width.precisionf}

result = 100/777

print(result)

print("The result is {}".format(result))

print("The result is {r:1.3f}".format(r=result))

#USING FORMATTED STRING LITERALS

name = "Jose"

print(f"His name is {name}")

name = "Sam"
Age = 6
School = "Buddo Jr"
Best_Dish = "Rice"

print(f"{name} is P{Age} years old, he studies at {School} and his best dish is {Best_Dish}.")

name = 'Aisha'
school = 'ST.George'
age = 18
combination = 'LAD'

print(f'My name is {name} and I am {age} years old. I school at {school} and I offer {combination}.')
