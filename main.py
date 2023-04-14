# juego piedra papel o tijera, del curso introduccion a python platzi

# logica de programacion
# se eleijen las opciones de cada jugador

# user_option = input('piedra, papel o tijera? => ')
# computer_option = 'piedra'

# #se evaluan las dos opciones
# if user_option == computer_option:
#   print('empate')
# elif user_option == 'piedra':
#   if computer_option == 'tijera':
#     print('tijera pierde con piedra')
#     print('user win')
#   else:
#     print('papel gana a piedra')
#     print('computer win')

# elif user_option == 'papel':
#   if computer_option == 'tijera':
#     print('tijera gana ha papel')
#     print('computer win')
#   else:
#     print('piedra pierde con papel')
#     print('user win')

# elif user_option == 'tijera':
#   if computer_option == 'piedra':
#     print('piedra gana ha tijera')
#     print('computer win')
#   else:
#     print('papel pierde con tijera')
#     print('user win')

# utlizando las tuplas
import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

rounds = 1

while True:

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)

    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    rounds += 1

    if not user_option in options:
      print('esa opcion no es valida')
      continue

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computer gano!')
            computer_wins += 1

    if computer_wins == 2:
      print('El ganador es la computadora')
      break

    if user_wins == 2:
      print('El ganador es el usuario')
      break

    
