# if el indentado me marca a que bloque de ejecucion pertenece la siguiente instruccion
#-------------o-------------------------------
#if{codigo} si es verdadero se ejecuto sino pasa al siguiente if
#if{codigo}
#-------------o-------------------------------
# if{codigo}
# elif{codigo}(implicito cuando hay que evaluar una siguiente condicion)
#-------------o-------------------------------
# if{codigo}
# else:{codigo}(sino explisito)
'''
if True:
  print('esto se debe ejecutar si es verdadero')

if False:
  print('aqui es falso, no ejecuto el bloque anterior')

# si sencillo

mascota = input('ingresa tu mascota => ')

if mascota == 'perro':
  print('es mi mascota preferida')
 
if mascota != 'perro'::
  print('es mi mascota no tan preferida') 
'''

stock = int(input('digite cant de unidades => '))

if stock >= 100 and stock <= 1000:
  print('stock valido, ten buen dia')
'''
# si sino da una alternativa a un valor negativo
if mascota == 'perro':
  print('es mi mascota preferida')
 
else:
  print('es mi mascota no tan preferida') 
'''

stock = int(input('digite cant de unidades => '))

if stock >= 100 and stock <= 1000:
  print('stock valido, ten buen dia')
elif stock == 0:
  print('stock invalido, ojo hay un robo, inventario no puede ser 0')
elif stock >= 1000:
  print(
    'stock sbrocargado, ojo hay que vender, inventario no puede ser tan alto')
