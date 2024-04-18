#Ejercicio 4

#Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.
num_inputs = int(input("How many numbers do you want to enter? "))

sum_of_numbers = 0

for _ in range(num_inputs):
    number = float(input("Enter a number: "))
    sum_of_numbers += number
