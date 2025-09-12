#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
'''for i in range(101):
    print(i)'''
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.
'''num = int(input("ingrese un numero"))
dig = len(str(num))
print(f"el numero tiene {dig} digitos")'''
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores. 
'''num1 = int(input("ingrese un numero"))
num2 = int(input("ingrese otro numero"))
res = 0
if num1 < num2:
    num1 = num1 + 1
    while num1 != num2:
        res = res + num1
        num1 = num1 + 1
elif num1 > num2:
    num1 = num1 - 1
    while num1 != num2:
        res = res + num1
        num1 = num1 - 1
else:
    pass
print(res)'''
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 
'''inp = int(input("ingrese un numero"))
res = 0
while inp != 0:
    res = res + inp
    inp = int(input("ingrese un numero"))
print(res)'''
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
