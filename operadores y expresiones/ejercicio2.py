#Ejercicio 2

#Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).
     
user_input = input("ingrese cadena de texto: ")
if len(user_input) >= 3 and len(user_input) < 10:
    print(True)
else:
    print(False)