set_countries = {'col', 'mex', 'bol', 'col'}

# Ver la cantidad de Elementos
size = len(set_countries)
print(size)

# Preguntar sobre un elemento en especifico
print('col' in set_countries)
print('pe' in set_countries)

# Adicionar
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# Actualizar Elementos
set_countries.update({'ar', 'ec', 'pe'})
print(set_countries)

# Eliminar elementos
set_countries.remove('col')
print(set_countries)

set_countries.remove('ar')
print(set_countries)

set_countries.discard('arg')
print(set_countries)

set_countries.add('arg')
print(set_countries)

# Eliminar todo el conjunto
set_countries.clear()
print(set_countries)