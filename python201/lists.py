numbers = []
for element in range(1,11):
    numbers.append(element * 2)

print(numbers)

# Se reduce con List Comprehension
numbers_v2 = [element for element in range(1,11)]
print(numbers_v2)

numbers_v3 = [element * 2 for element in range(1,11)]
print(numbers_v3)

# Utilizando una condicion, froma clasica
numbers_v4 = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers_v4.append(i*2)

print(numbers_v4)

# Utilizando List Comprehension
numbers_v4 = [i*2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v4)