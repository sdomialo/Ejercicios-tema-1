#Ejercicio 2

#Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.

while True:
    num = int(input("Introduce un número impar: "))
    if num % 2 != 0:
        break
    else:
        print("El número introducido no es impar. Intenta de nuevo.")

print("Número impar introducido correctamente:", num)