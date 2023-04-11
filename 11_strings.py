# mas metodos para strings
text = "intentando aprender phyton para mi postulacion a Talento B de bancolombia"

print(text)
# in me permite saber si hay un texto en una cadena de text, responde true o false
print('phyton' in text)

# len nos genera el taaño de un string e incluye los espacios
print(len(text))

# lupper convierte el texto a mayusculas
print(text.upper())

# lower convierte el texto a minusculas
print(text.lower())

#count permite saber el numero de veces que aparece un caracter en un cadena
print(text.count(" "))

#sapcase convierte de mayusculas a minusculas y viceversa
text = "cadena de PRUEBA"
print(text.swapcase())

# startswiith o endswith si el texto inicia o finaliza con un texto especifico
print(text.startswith('hola'))
print(text.endswith('PRUEBA'))

# replace me perm ite cambiar un caracter o cadena por otra txt.replace(el que buscao, el que reemplaza)
text = "busco participar del proceso de talento B de bancolombia"
print(text.replace('busco participar del ', 'logré ser contratado en '))

#capitalize cambia el primer caracter en mayusculas de una cadena de texto y los demas en minusculas
print(text.capitalize())

#title cambia el primer caracter de todas las palabras de una cadena de texto a mayusculas
print(text.title())

#isdigit evalua si es un numero con formato de texto
print('3956'.isdigit())
