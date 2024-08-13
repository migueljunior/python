# Show Message
print("Hey, I'm a message in your console!")

# Variables
name = "Junior"
print("Hey, I'm showing the next variable: " + name)

# String type
# To ask the type of variable we can use the function type
type_name = str(type(name))
print("The variable name with value " + name + " is type " + type_name)

# You can declare String in the next three modes
mode_1 = "Hi"
mode_2 = 'Hello again'
mode_3 = '''This is the last time I say hello'''

# We can use the index of String similar as an array
testing = "I am a long String"
print(testing[3])
print(testing[5])
print(testing[-1])
print(testing[-6])

# Replicate the string 5 times
print(5 * mode_1)

# Count the characters
print(len(mode_3))
print(len(mode_1))

# Integer type
x = 10
print(x)
print(type(x))

# Float type
y = 5.6539
print(y)
print(type(y))
z = 1.54e7
print(z)
a = 34.6e-6
print(a)

# Boolean type
is_true = True
print(is_true)
print(type(is_true))
is_false = False
print(is_false)
print(type(is_false))