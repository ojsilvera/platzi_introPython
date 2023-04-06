#and
print('AND')
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)

print(10 > 5 and 2 < 8)

stock = input('digite cant de unidades => ')
stock = int(stock)

print(stock >= 100 and stock <= 1000)

#or
print('*' * 10)
print('OR')
print('*' * 10)

print('True and True =>', True or True)
print('True and False =>', True or False)
print('False and True =>', False or True)
print('False and False =>', False or False)

role = input('Digita rl rol => ')

print(role == 'admin' or role == 'seller')

# not
print('*' * 10)
print('NOT')
print('*' * 10)
print(not True)
print(not False)

print('NOT-AND')
print('not True and True =>', not (True and True))
print('not True and False =>', not (True and False))
print('not False and True =>', not (False and True))
print('not False and False =>', not (False and False))

print(not(10 > 5 and 2 < 8))

stock = input('digite cant de unidades => ')
stock = int(stock)

print(not(stock >= 100 and stock <= 1000))
