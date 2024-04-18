#Ejercicio 6

#Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?

#Nombre Apellido ha sacado un Nota de nota.

#Ayuda

#Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]

cadena = "zereP nauJ,01"

cadena = "zereP nauJ,01"

# Split the string into name and grade
name, grade = cadena[::-1].split(',')

# Format the string
formatted_string = f"{name[::-1]} ha sacado un Nota de {grade[::-1]}."

# Print the formatted string
print(formatted_string)

#Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]
