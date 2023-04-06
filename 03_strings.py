# imprimir
name = "Oscar"
last_name = "Silvera"
print(name)
print(last_name)

# concatenar
full_name = name + " " + last_name
print(full_name)

# insertando variables en frases y hacerlas dinamicas

# la f delante le indica que es un texto con formato y el parametro va entre {}
template = f"hola, yo soy {full_name}, candidato ha data science en talento B 2023 "

print(template)

# con la funcion format al final igual que el ejemplo anterior, pasamos el valor y las {}
# ubican donde va
template2 = "hola, yo soy {}, candidato ha data science en talento B 2023 ".format(
  full_name)

print(template2)
