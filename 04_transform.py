name = "Oscar"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

#para convertir a entero
name = str(12)
print(type(name))

#convierto a entero el string anterior
print(type(int(name)))

#input para introducir la edad da como resultado un string siempre
age = input('escribe tu edad => ')

#aqui el resultado es un string
print(type(age))

#aca convierto momentaneamente age de str a int
print(f'Tu edad en 10 años será {int(age) + 10}')

#aca convierto permanentemente age de str a int
age = int(age)
print(type(age))
