# CRUD Create, Read, Update & Delete

numbers = [1, 2 , 3 , 4 , 5]
print(numbers[1])

numbers[-1] = 10
print(numbers)

numbers.append(700) #agrega un nuevo elemento al final del vector
print(numbers)

numbers.insert(0, 'hola') #lista.insert(posicion, elementoHaInsertar)
print(numbers)

numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks #une las vector 
print(new_list)

index = new_list.index('todo 2') #nos muestra la posicion de un elemento de la vector
new_list[index] = 'todo changed' #reemplaza el elemento que se encuentra en la posicion almacenada en index
print(new_list)

new_list.remove('todo 1') #elimina un elemento en especifico
print(new_list)

new_list.pop() #elimina el ultimo delemento en una vector
print(new_list)

new_list.pop(0) #elimina un elemento en una posicion determinada
print(new_list)

new_list.reverse() #invierte una vector
print(new_list)

numbers_a = [1, 4, 6 , 3] #ordena una vector en forma desencdente, con mas de n tipo de dato en la vector no lo puede ordenar
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

new_list.sort()