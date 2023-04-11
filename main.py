# juego piedra papel o tijera, del curso introduccion a python platzi

# logica de programacion
# se eleijen las opciones de cada jugador

user_option = input('piedra, papel o tijera? => ')
computer_option = 'piedra'

#se evaluan las dos opciones
if user_option == computer_option:
  print('empate')
elif user_option == 'piedra':
  if computer_option == 'tijera':
    print('tijera pierde con piedra')
    print('user win')
  else:
    print('papel gana a piedra')
    print('computer win')

elif user_option == 'papel':
  print('computer win')
