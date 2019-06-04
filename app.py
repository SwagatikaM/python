print("Swagatika Mahapatra")
print('o----')
print(' ||||')
print('*' * 10)

#Variables
price=10
rating=4.9
name='Swagatika'
is_published=True
print('price:', price, '\n', 'rating:', rating, '\n', 'name:', name, '\n', 'is_published:', is_published)

#Inputs
#name = input('What is your name? ')
#print('Hi ' + name)

#Type Conversions
#birth_year = input('Birth year: ')
#print(type(birth_year))
#age = 2019 - int(birth_year)
#print(type(age))
#print(age)

#Negative array indices possible
course = 'Python for Beginners'
print(course[1])
print(course[0])
print(course[-1])
print(course[-2])
print(course[-20])

print(course[1:5])
coursetwo = course[:]
print(coursetwo)
print(course[1:-1])

#Formatted Strings
first = 'Swagi'
last = 'Mahapatra'

msg = f'{first} [{last}] is a coder'
print(msg)
print(len(msg))

#Upper method  creates another string
print(course.upper())

print(course.find('o'))
print(course.title())
print(course.replace('Beginners', 'Absolute Boginners'))
print(course)
print('Python'in course)

#Integres in Pyhton
print(10/3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

#MATH
x = 2.9
print(abs(-2.9))
print(round(2.9))

import math
print(math.floor(x))


#If statements
is_hot = False
is_windy = False

if is_hot:
    print('Its a hot day!')
    print('Drink plenty of water!')
elif is_windy:
    print('Its a windy day!')
    print('wear a windcheater!')
else:
    print('Its a cold day!')
    print('Wear warm clothese')
print('Enjoy the day')

#Calc down payment

price = 1000000
has_good_credit = True
has_high_income = True

if has_good_credit and has_high_income:
    down_payment =  0.1 * price
else:
    down_payment =  0.2 * price
print(f'Down Payment: {down_payment}')

#Logicaloperators  - and, or, not

has_criminal_record = False

if has_high_income and has_good_credit and not has_criminal_record:
    print('Eligible for loan!')

#Comparison operators : >, <, >=, <=, ==, !=

#While loop
command = ""
started = False

while True:
    command = input(" > ")
    if command == "start":
        if not started:
            print("Car started!")
            started = True
        else:
            print("Car is already started!")
    elif command == "stop":
        if started:
            print("Car stopped!")
            started = False
        else:
            print("Car is already stopped!")
    elif command == "help":
        print("""
     start - to start tyhe car
     stop - to stop the car
     quit - to quit""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand!")









   



