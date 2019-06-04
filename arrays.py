numbers = [2, 4, 6, 1, 8, 9, 22, 54, 5, 3]

numbers.sort()
print(numbers[-1])

max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#Matrix in Python - 2D array

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)