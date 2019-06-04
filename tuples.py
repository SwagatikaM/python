#Tuple are immutable , but like list

numbers = (1, 2, 3)

print(numbers[1])
print(numbers.count)
# Number s cannot be assigned, added or removed

#Unpacking applicable to tuple and list
coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# same as above
x, y, z = coordinates
