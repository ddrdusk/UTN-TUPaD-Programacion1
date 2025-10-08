# 1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.
'''def imprimir_hola_mundo():
    print("“Hola Mundo!”")
imprimir_hola_mundo()'''
#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.
'''def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
saludar_usuario(input("Ingrese nombre "))'''
#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores 
#ingresados.
'''def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
a , b, c, d = input("ingrese nombre, apellido, edad y residencia (separados por un espacio)").split()
informacion_personal(a , b, c, d)'''
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    print("el radio es: ")
def calcular_perimetro_circulo(radio):
    print("el perimetro es: ")
radio = int(input("ingrese el radio "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)