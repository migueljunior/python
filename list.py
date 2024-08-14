# The list is very similar as an Array
to_do = ["Go to hotel",
         "Go to lunch",
         "Visit a Museum",
         "Come back to hotel"]
print(to_do)

# They can save a different types of data
numbers = [1,2,3,4, "five"]
print(numbers)
print(type(numbers))

mix = ["one", 2, 3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print("First element =>", mix[0])
print("Second element =>", mix[1])
print("Last element =>", mix[-1])

string = 'Hello World'
print("First element =>", string[0])
print("Second element =>", string[1])
print("Last element =>", string[-1])

# Slicing
print(mix[0:2])

# Adding data at the last into the list
print(mix)
mix.append(False)
print(mix)
mix.append(['a','b'])
print(mix)

# Adding into a specific position in this case 1
mix.insert(1,"Testing")
print(mix)

# We can get the specific index of data
print(mix.index("Testing"))
print(mix.index(['a','b']))

# We can get the max and min minor from a list
numbers = [1,200,34,90,5,24,90]
print("Max is =>",max(numbers))
print("Minor is =>",min(numbers))
# The index method only returns the first coincidence
print(numbers.index(90))

# Delete specific element or range of elements from the list
print(numbers)
del numbers[-1]
print(numbers)
del numbers[1:2]
print(numbers)
# Delete complete list
del numbers

# To copy the information from any list into another list
a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
print(a)
print(b)

# This is showing the space in memory
print(id(a))
print(id(b))

# We need use slice to copy only the information
print('Using slice method:')
c = a[:]
print('List a:',a)
print('List b:',b)
print('List c:',c)
print('Deleting position 1 of list a')
del a[1]
print('List a:',a)
print('List b:',b)
print('List c:',c)
print('Printing space in memory:')
print('Space list a:',id(a))
print('Space list b:',id(b))
print('Space list c:',id(c))