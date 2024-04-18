#Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

#Todos los números del 0 al 10 [0, 1, 2, ..., 10]

#Todos los números del -10 al 0 [-10, -9, -8, ..., 0]

#Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]

#Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]

#Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

#Se pueden generar saltos en el range() estableciendo su tercer parámetro range(inicio, fin, salto), experimenta.

# Todos los números del 0 al 10
numbers_0_to_10 = list(range(11))
print(numbers_0_to_10)

# Todos los números del -10 al 0
numbers_minus_10_to_0 = list(range(-10, 1))
print(numbers_minus_10_to_0)

# Todos los números pares del 0 al 20
even_numbers_0_to_20 = list(range(0, 21, 2))
print(even_numbers_0_to_20)

# Todos los números impares entre -20 y 0
odd_numbers_minus_20_to_0 = list(range(-19, 0, 2))
print(odd_numbers_minus_20_to_0)

# Todos los números múltiples de 5 del 0 al 50
multiples_of_5_0_to_50 = list(range(0, 51, 5))
print(multiples_of_5_0_to_50)
