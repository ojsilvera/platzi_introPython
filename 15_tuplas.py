# las tuplas se diferencian de las listas o vectore, en que las tuplas no pueden ser cambiadas, por eso se dice que son 
#inmutables.
# otra diferencia las tupas son con parentecis y no con corchetes ocmo las listas

numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')
print(numbers)
print('0 =>', numbers[0]) # para acceder a un valor de la tupla, es el mombre de la tupla y entre corchetes el idice de la posicion que queremos
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# CRUD
# numbers.append(10)
print(numbers)
# numbers[1] = 'change'

print(strings)
print(strings.index('zule'))
print(strings.count('nico'))

my_list = list(strings) #Convierte una tupla en lista para hacer procesos de transformacion
print(my_list)
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)