set_countries = {'col', 'mex', 'bol', 'col'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)
print(type(set_numbers))

set_types = {1, 'hola', False, 12.2}
print(set_types)

set_from_string = set('hola')
print(set_from_string)

set_from_tuple = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuple)

numbers = [1,2,3,1,3,4,5]
set_from_list = set(numbers)
print(set_from_list)
unique_numbers = list(set_from_list)
print(unique_numbers)