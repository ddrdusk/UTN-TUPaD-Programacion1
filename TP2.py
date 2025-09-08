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
'''import random
from statistics import mode, median, mean 
num =  [random.randint(1, 100) for i in range(50)]
if(mean(num) > median(num) > mode(num)):
    print("sesgo positivo")
elif(mean(num) < median(num) < mode(num)):
    print("sesgo negativo")
elif(mean(num) == median(num) == mode(num)):
    print("sin sesgo")
else:
    print("???")'''
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla. 
'''stri = input("Ingrese una frase.")
ult = stri[len(stri) - 1]
def isvow(letter):
    voc = {"a","i","u","e","o","A","I","U","E","O"}
    return letter in voc
if(isvow(ult)):
    print(stri + "!")
else:
    print(stri)'''
#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
'''nom = input("ingrese su nombre")
styl = int(input("elija su estilo (1, 2, o 3)"))
if(styl == 1):
    print(nom.upper())
elif(styl == 2):
    print(nom.lower())
elif(styl == 3):
    print(nom.title())
else:
    print("ERROR")'''
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 
'''UDontBelongInThisWrld = float(input("Ingrese la magnitud del terremoto. "))
if(UDontBelongInThisWrld < 3):
    print("Muy leve")
elif(UDontBelongInThisWrld >= 3 and UDontBelongInThisWrld < 4):
    print("Leve")
elif(UDontBelongInThisWrld >= 4 and UDontBelongInThisWrld < 5):
    print("Moderado")
elif(UDontBelongInThisWrld >= 5 and UDontBelongInThisWrld < 6):
    print("Fuerte")
elif(UDontBelongInThisWrld >= 6 and UDontBelongInThisWrld < 7):
    print("Muy Fuerte")
else:
    print("Extremo")'''
#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano. 
'''hemi = input("Ingrese su hemisferio")
mes = int(input("Ingrese el mes (numero)"))
dia = int(input("Ingrese el dia (numero)"))
def nordie(letter):
    North = {"n","N","north","North","NORTH"}
    return letter in North
def suddey(letter):
    South = {"s","S","south","South","SOUTH"}
    return letter in South
if nordie(hemi):
    if ((mes == 12 and dia >= 21) or mes < 3 or (mes == 3 and dia <= 20)):
        print("Invierno")
    elif(6 > mes > 3 or (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20)):
        print("Primavera")
    elif(9 > mes > 6 or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20)):
        print("Verano")
    elif(12 > mes > 9 or (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20)):
        print("Otoño")
    else:
        print("Error con el mes o dia")
elif suddey(hemi):
    if ((mes == 12 and dia >= 21) or mes < 3 or (mes == 3 and dia <= 20)):
        print("Verano")
    elif(6 > mes > 3 or (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20)):
        print("Otoño")
    elif(9 > mes > 6 or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20)):
        print("Invierno")
    elif(12 > mes > 9 or (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20)):
        print("Primavera")
    else:
        print("Error con el mes o dia")
else:
    print("Error con el hemisferio")'''