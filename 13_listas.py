# reemplazo de un caracter en una posicion determinada
text = 'Hola'
new_text = 'W' + text[1:]
print(text) 
print(new_text) 

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1.5, 2.8]
print(nums[5:8]) 
# nueva tupla con inicio en 126 y las posicion (i:f-1(6,7,8)) => [126, 6, 7, 8]
print( [126] + nums[5:8]) 

lista = [1,2,3,4,5,6,7,8,9]
print(lista[1])   #salida:2
print(lista[1:6]) #Devuelve: [2, 3, 4, 5, 6]
print(lista[-3])  #salida : [7]

#La lista NO es inmutable, es decir, permite modificar los datos que han sido creados. Ejemplo
lista = [1,2,3,4,5,6,7,8,9]
lista[2] = 3.8 #Ahora 3.8 es el tercer elemento
print(lista)

# Permiten agregar nuevos valores. Ejemplo:
lista.append('Nuevo Dato')
print(lista)

numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1, True, 'hola']
print(types)

print(numbers[0])
print(tasks[0])
text = 'Hola'
# text[0] = 'W'

tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

print(numbers[:3])
print(True in types)
print('hola' in types)