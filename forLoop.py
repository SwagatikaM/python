# For loop

for item in 'Python':
    print(item)

for item in ["one", "two", "three"]:
    print(item)

for item in [1,2,3]:
    print(item)

for item in range(10):
    print(item)

for item in range(5, 15, 2):
    print(item)

#Adding prices
prices = [10, 20, 30]

total = 0
for price in prices:
    total += price

print(f"Total is {total}")

#Nested Loops
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

#Priniting an F

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    output = ''
    for count in range(number):
        output += 'X'
    print(output)