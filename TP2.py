#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
'''edad = int(input("ingrese su edad"))
print("Es mayor de edad") if edad > 18 else print("no es mayor de edad")'''
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”. 
'''nota = int(input("ingrese su nota"))
print("Aprobado") if nota >= 6 else print("Desaprobado")'''
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar. 
'''num = int(input("ingrese un numero par"))
print("Ha ingresado un número par") if num % 2 == 0 else print("Por favor, ingrese un número par")'''
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.
'''edad = int(input("ingrese su edad"))
if (edad < 12):
    print("Niño")
elif(edad >= 12 and edad < 18):
    print("Adolescente")
elif(edad >= 18 and edad < 30):
    print("Adulto joven")
else:
    print("Adulto")'''
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string.
'''passw = len(input("ingrese su contraseña"))
print("Ha ingresado una contraseña correcta") if passw <= 14 and passw >= 8 else print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")'''
#6)Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
#Definir la lista numeros_aleatorios de la siguiente forma: 
#import random 
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
#forma aleatoria.
