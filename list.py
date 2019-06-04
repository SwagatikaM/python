numbers = [2,4,6,3,7]
numbers.insert(0, 10)
print(numbers)

numbers.remove(10)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(6))
print(numbers.count(6))
print(50 in numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()


# Removing duplicates off a list

numbers = [2, 54, 2, 5, 7, 6, 3, 8, 91, 9, 4, 9, 13, 2, 4]
unique =[]

for number in numbers:
    if number not in unique:
        unique.append(number)
print(f"Unique list : {unique}")