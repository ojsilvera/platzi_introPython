# CRUD Create, Read, Update & Delete

numbers = [1, 2 , 3 , 4 , 5]
print(numbers[1])

numbers[-1] = 10
print(numbers)

numbers.append(700) #agrega un nuevo elemento al final de la tupla
print(numbers)

numbers.insert(0, 'hola') #lista.insert(posicion, elementoHaInsertar)
print(numbers)

numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks #une las tuplas 
print(new_list)

index = new_list.index('todo 2') #nos muestra la posicion de un elemento de la tupla
new_list[index] = 'todo changed' #reemplaza el elemento que se encuentra en la posicion almacenada en index
print(new_list)

new_list.remove('todo 1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [1, 4, 6 , 3]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

new_list.sort()