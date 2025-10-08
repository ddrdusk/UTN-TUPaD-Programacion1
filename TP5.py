#1. Crear una función llamada imprimir_hola_mundo que imprima por
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
#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el 
#radio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar 
#ambas funciones para mostrar los resultados.
'''def calcular_area_circulo(radio):
    area = 3.14 * (radio ** 2)
    print(f"el area es: {area}")
def calcular_perimetro_circulo(radio):
    perimeter = 2 * 3.14 * radio
    print(f"el perimetro es: {perimeter}")
radio = int(input("ingrese el radio "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)'''
#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y 
#mostrar el resultado usando esta función.
'''def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"Pasaron {horas} horas")
segundos_a_horas(int(input("cuantos segundos pasaron ")))'''
#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la 
#función.
'''def tabla_multiplicar(numero):
    for i in range(10):
        print(numero * (i + 1))
tabla_multiplicar(int(input("ingrese numero ")))'''
#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado 
#de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los 
#resultados de forma clara.
'''def operaciones_basicas(a , b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b
    print(f"El resultado de la suma es {suma}")
    print(f"El resultado de la resta es {resta}")
    print(f"El resultado de la multiplicacion es {mult}")
    print(f"El resultado de la division es {div}")
num1 = int(input("ingrese el primer numero "))
num2 = int(input("ingrese el segundo numero "))
operaciones_basicas(num1 , num2)'''
#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la 
#función para mostrar el resultado con dos decimales.