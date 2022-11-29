# Python 101
La extencion de los archivos python es **.py**
En python es muy importante la identacion para los bloques de codigo.
Para agregar comentarios se utiliza el caracter hastag como se muestra a continuacion:

``#Esto es un comentario``

Para realizar un comentario de varias lineas se utiliza 3 comillas (puede ser simple o doble):

```
"""
Comentario de
Varias lineas
"""
```

### Variables
Es un espacio de memoria en el cual se guarda un determinado tipo de dato.

### Tipos de Datos
Para conocer el tipo de dato se puede utilizar la siguiente funcion:
```
type(variable)
```
- string => es Una cadena de texto, se puede usar comillas simple y dobles.
- int => Entero
- boolean => Es un booleano y solo puede tener True o False

### Strings
Para realizar concatenacion de texto se puede realizar de la siguente manera:
```
name = 'Nicolas'
last_name = 'Molina Monroy'
full_name = name + " " + last_name
print(full_name)
```
Para poder realizar apostrofes en la cadena de estring se puede utilizar un mix entre comillas dobles y comillas simples.

Para darle un formato se puede utilizar lo siguiente:
```
template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
template_1 = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
```

### Numbers
Existen los siguientes tipos:
- int => Enteros, 3
- float => Numeros con presicion decimal, 12.45

### Booleans
Este tipo de dato simplemente almacena dos estados True o False

### Transformacion de Tipos
Se puede convertir los tipos de datos de manera dinamica de las siguientes maneras:
```
name = 'Nicolas'
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))
```
Convertir entero a string:
```
age = 12
print("Mi edad es " + str(age))
```
Convertir string a entero:
```
age = "12"
int(age)
```
Mayor informacion de casting en python ver el siguiente [link](https://www.w3schools.com/python/python_casting.asp)

### Operadores Aritmeticos
Los operadores aritmeticos son los siguientes:
- (+) Suma
- (-) Resta
- (*) Multiplicación
- (/) División
- (%) Modulo o Residuo
- (//) Division deonde el resultado es el valor entero
- (**) Exponenciación

Prioridad de las operaciones aritmeticas son las siguientes:
- P - Parentesis
- E - Exponentes
- M - Multiplicacion
- D - Division
- A - Adicion
- S - Sustraccion

### Operadores de comparacion
Estos son los operadores de comparacion:
- ( > / < ) Mayor / Menor
- ( >= / <= ) Mayor o igual / Menor o igual
- ( == ) Igual
- ( != ) Diferente

Para la comparacion de flotantes pues al tener presicion diferente se puede caer en errores de manera facilmente, para evitar estos errores se puede comparar de la siguiente manera:
```
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)
#Forma no matematica
y_str = format(y,".2g")
print('str =>', y_str)
print(y_str == str(x))
#Forma matematica
print(y, x)
tolerance = 0.0001
print(abs(x-y) < tolerance)
```
### Operadores logicos
| Operador | Descripcion | Ejemplo |
|----------|-------------|---------|
|and |Returns True if both statements are true|x < 5 and  x < 10|
|or |Returns True if one of the statements is true|x < 5 or x < 4|
|not|Reverse the result, returns False if the result is true|not(x < 5 and x < 10)|

Para mayor informacion se puede ver el siguiente [link](https://www.w3schools.com/python/python_operators.asp)

### Condicionales
Basandonos en preguntas decimos al programa de bloque de codigo se deberia ejecutar, para mayor informacion puede ver el siguiente [link](https://www.w3schools.com/python/python_conditions.asp)

### String Recargado
Los strings tienen distintos metodos para el manejo de los mismos, por ejemplo:
- Encontrar una palabra dentro de un texto
```
text = 'Ella sabe programar en Python'
print('Javascript' in text)
print('Python' in text)
```
- Contar la cantidad de caracteres
```
size = len(text)
print(size)
```
- Pasar a mayusculas
```
print(text.upper())
```
- Pasar a minusculas
```
print(text.lower())
```
- Contar cantidad de apariciones de un caracter
```
print(text.count('a'))
```
Para mayor informacion puede ver el siguiente [link](https://www.w3schools.com/python/python_strings_methods.asp)

### Indexing y slicing
Indexing significa que los textos tienen un indicador que se puede acceder a traves de posiciones, por ejemplo:
```
text = 'Ella sabe Python'
print(text[0])
print(text[1])
print(text[999])
size = len(text)
print('size =>',size)
print(text[size - 1])
#Python puede empezar de manera negativa a partir del ultimo caracter
print(text[-1])
```
Slicing es poder extraer una parte del texto a partir de las posiciones
```
print(text[0:5])
print(text[10:16])
print(text[:10])
print(text[5:])
print(text[:])
#print(text[Inicio:Final:Cantidad de saltos])
print(text[10:16:2])
print(text[::2])
```
### Listas
Es una estructura de datos que mas se utiliza, esta puede ser modificada, cada elemento es separado por una coma y puede contener todo tipo de datos.
```
numbers = [1,2,3,4]
tasks = ['make a dishes', 'play videogames']
types = [1, True, 'hola']
```
Se puede imprimir/actualizar cada elemento segun la posicion en la que se encuentre.
Existen distintos tipos de metodos que se pueden utilizar con las listas:

**Metodos:**
- Lista.metodo(indice,elemento) o Lista.metodo(elemento)

**Metodos importantes**
- .count(elemento) cuenta cuantas veces un elemento esta en una lista
- .extend(lista) permite extender una lista agregándole los elementos de otra lista
- .pop() elimina y retorna el ultimo elemento de la lista
- .reverse() reversa el orden de la lista
- .sort() ordena la lista de manera ascendente o descendente

**Actualizar un valor**
```
Lista = [1, 2, 3, 4, 5]
Lista[0] = -8
Lista = [-8, 2, 3, 4, 5] #resultado de la lista luego de actualizar el valor
```
**Agregar un elemento**
- lista.insert(indice,elemento)
- Lista.append(indice,elemento)
- Lista.append(elemento) en este caso el nuevo elemento se agrega al final de la lista

**Eliminar un elemento**
- Lista.remove(elemento)
- Lista.remove(indice, elemento)

**Buscar el indice del elemento**
- lista.index(elemento)

Para mayor informacion puede ver el siguiente [link](https://www.w3schools.com/python/python_lists.asp)

### Tuplas
Para declararlo se lo realiza parecido a la lista con la diferencia que se utiliza parentesis, tambien esta estructura es inmutable.
```
numbers = (1,2,3,4)
strings = ('nico', 'zule', 'sante')
```
En la tupla simplemente se lo realiza en la declaracion pero no se puede agregar mas, por lo que no tienen todos los metodos como con las listas, por lo que es una estructura de datos solo de letura.

Los unicos metodos que se puden utilizar en una tupla son:
- index
- count
- convertirla a lista y viceversa

Para mayor informacion puede ver el siguiente [link](https://www.w3schools.com/python/python_tuples.asp)

### Diccionarios
Esta estructura se comporta como un diccionario el cual utiliza una llave como palabra y cada llave tiene un valor.
```
my_dict = {}
print(type(mydict))

my_dict = {
    'avion': 'bla bla bla',
    'name': 'Nicolas',
    'last_name': 'Molina Monroy',
    'age': 87
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])#Si la llave no se encuentra dara un error
print(my_dict.get('age'))# En el caso que no exista la llave dara como resultado None
print('avion' in my_dict)
```
#### Insercion y actualizacion en diccionario
```
person = {
    'name': 'nico',
    'last_name': 'molina',
    'langs': ['python','javascript'],
    'age': 99
}

print(person)
person['name'] = 'santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)

del person['last_name']
person.pop('age')
print(person)

print('Items')
print(person.items())#Devuelve en tuplas

print('Keys')
print(person.keys())

print('Values')
print(person.values())
```

### Loops: While
Este ciclo se ejecuita mientras una condicional sea verdadera:
```
#Este es un ciclo infinito
while True:
    print('Se ejecuto')
```

Ejemplo:
```
counter = 0
while counter < 10:
    counter++
    print(counter)
```
Manera de romper el while antes de que cumpla la condicion:
```
counter = 0
while counter < 20:
    counter++
    if counter == 15:
        break
    print(counter)
```
Con la palabra reservada break se saldra del ciclo, en este caso cuando counter sea 15.
```
counter = 0
while counter < 20:
    counter++
    if counter == 15:
        continue
    print(counter)
```
La palabra reservada hace que salte al siguiente iteracion del siclo sin ejecutar lo que continue en el bloque de codigo

### Loops: For
Este se utiliza cuando se tiene claro cuantas veces se desea iterar, ejemplo:
```
for element in range(1, 20):
    print(element)
```
Ejemplo utilizando una lista:
```
my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)
```
Ejemplo utilizando una tupla:
```
my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
    print(element)
```
Ejemplo utilizando un diccionario:
```
product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}
for element in procut:
    print(product[element])

for key, value in product.items():
    print(key, '=>', value)
```
Ejemplo mas complejo, lista de diccionarios:
```
people = [
    {
        'name': 'nico',
        'age': 34
    },
    {
        'name': 'zule',
        'age': 45
    },
    {
        'name': 'santi',
        'age': 4
    }
]
for person in people:
    print(person)
    print('name =>',person['name'])
```
### Ciclos anidados
Los ciclos pueden ser anidados es decir que puede existir 1 ciclo dentro de otro ciclo, esto dependiendo a la situacion que se desea resolver.
```
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz[0])
print(matriz[0][1])

for row in matriz:
    print(row)
    for column in row:
        print(item)
```