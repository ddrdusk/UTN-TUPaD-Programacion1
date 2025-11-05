#1) Dado el diccionario precios_frutas 
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
#Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 ● Manzana = 1500 ● Pera = 2300
'''precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300'''
#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 ● Manzana = 1700 ● Melón = 2800 
'''precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800'''
#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. 
'''lista = precios_frutas.keys()'''
#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
'''direct = {}
for i in range(5):
    contct = input("Ingresa un nombre ")
    num = int(input("Ingresa su numero "))
    direct[contct] = num
contct = input("Cual contacto? ")
if contct in direct:
    print(direct[contct])
else:
    print("error")'''
#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra.
'''fras = input("Ingrese una frase ")
palab = fras.split()
palaSet = set(palab)
palaCont = {}
for i in palab:
    if i in palaCont:
        palaCont[i] += 1
    else:
        palaCont[i] = 1
print(palaSet)
print(palaCont)'''
#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno.
'''from statistics import mean
notas = {}
for i in range(3):
    alum = input("Ingresa un nombre ")
    nota = (int(input("Ingresa la nota ")), int(input("Ingresa la nota ")), int(input("Ingresa la nota ")))
    notas[alum] = nota
for i in notas:
    print(i)
    promed = mean(notas[i])
    print(promed)'''
#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. • Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
'''parc1 = (1,3,4,6)
parc2 = (2,3,5,6)
ambparc = []
aprob = set(parc1 + parc2)
for i in aprob:
    if i in parc1 and i in parc2:
        ambparc.append(i)
    else:
        pass
print(aprob)
print(ambparc)'''
#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: • Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. • Agregar un nuevo producto si no existe.
'''stock = {}
act = ""
while act != "4":
    print("")
    print("1. Consultar stock")
    print("2. Agregar unidades a stock")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    act = input("Que quiere hacer? ")
    if act == "1":
        product = input("Cual producto? ").lower()
        if product in stock:
            print(f"El producto {product} tiene {stock[product]} unidades")
        else:
            print(f"El producto '{product}' no está en el catalogo")
    elif act == "2":
        if len(stock) == 0:
            print("No hay stock")
        else:
            product = input("Que quiere suministrar ").lower()
            if product in stock:
                unid = int(input("Cuantas unidades? "))
                stock[product] += unid
                print(f"Hecho! Se han agregado {unid} unidades a {product}")
            else:
                print(f"El producto '{product}' no está en el catalogo")
    elif act == "3":
        product = input("Que producto desea agregar? ").lower()
        if product in stock:
            print(f"El producto '{product}' ya está en el catalogo")
        else:
            unid = int(input("Cuantas unidades desea agregar? "))
            stock[product] = unid
            print(f"Hecho! Se ha agregado {product} a catalogo")
    elif act == "4":
        print("Adios")
    else:
        print("Error! Elija otra opcion")'''
#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores.