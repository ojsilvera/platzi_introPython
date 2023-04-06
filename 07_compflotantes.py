x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)
y_str = format(y, ".2g")
print(type(y_str), y_str)
# la conversion de str a numero es con float
# porque es un numero decimal, si fuera base
# 10 seria con int
# una conversion de tipo temporal para ejecutar la comparacion
print(float(y_str) == x)
print('*' * 10)
# una conversion de tipo permanente
y_str = float(y_str)
print(type(y_str), y_str)
print(y_str == x)
