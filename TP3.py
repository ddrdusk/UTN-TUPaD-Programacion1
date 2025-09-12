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
'''import random
num =  random.randint(1, 9)
guess = int(input("Adivine un numero del 1 al 9~ "))
inten = 1
if(guess != num):
    while guess != num:
        guess = int(input("Equivocado~ Adivine otra vez~ "))
        inten = inten + 1
    print(f"Correcto~ Usted adivino en {inten} intentos~")
else:
    print(f"Correcto~ Usted adivino en {inten} intentos~")'''
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.
'''for i in range(100,0,-2):
    print(i)'''
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.
'''limit = int(input("1n6r3se un num3r0_"))
res = 0
for i in range(0,limit):
    res = res + i
print(res)'''
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio). 