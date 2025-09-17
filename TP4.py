#1) Crear una lista con las notas de 10 estudiantes. 
#• Mostrar la lista completa. 
#• Calcular y mostrar el promedio. 
#• Indicar la nota más alta y la más baja. 
'''from statistics import mean
notas = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
med = mean(notas)
for i in notas:
    print(notas[i])
print(f"promedio: {med}")
print(max(notas))
print(min(notas))'''
#2) Pedir al usuario que cargue 5 productos en una lista. 
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
'''list = []
for i in range(5):
    prod = input(f"ingrese producto {i+1}: " )
    list.append(prod)
print(list)
print(sorted(list))
borr = input("Que producto desea eliminar? ")
if borr in list:
    list.remove(borr)
    print(sorted(list))
else:
    print(sorted(list))'''
#3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
#• Crear una lista con los pares y otra con los impares. 
#• Mostrar cuántos números tiene cada lista. 
'''import random
list =  []
for i in range(15):
    numran = random.randint(1,100)
    list.append(numran)
print(f"1: {list}")
par = []
impr = []
print(list)
for num in list:
    if num % 2 == 0:
        par.append(num)
    else:
        impr.append(num)
print(f"2: {par}")
print(f"3: {impr}")'''
#4) Dada una lista con valores repetidos: 
#• Crear una nueva lista sin elementos repetidos. 
#• Mostrar el resultado. 
'''datos = [1 , 3 , 5 , 3 , 7 , 1 , 9 , 5 , 3]
list2 = []
for i in datos:
    if i in list2:
        pass
    else:
        list2.append(i)
print(datos)
print(list2)'''
#5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
#• Mostrar la lista final actualizada. 
'''list = ["Al" , "Baal" , "Cal" , "Dali" , "Earl" , "Far Quad" , "Gal" , "Lil' Hal"]
desic = int(input("Quiere agregar(1) o remover(0) a un estudiante? (si no quiere cambios entre otro numero)"))
if desic == 0:
    deth = input("Cual estudiante quiere eliminar?")
    if deth in list:
        list.remove(deth)
    else:
        print("Error. Cambio no efectuado")
elif desic == 1:
    add = input("Cual estudiante quiere eliminar?")
    list.append(add)
else:
    pass
for i in list:
    print(i)'''
#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero).
'''list = [1 , 2 , 3 , 4 , 5 , 6 , 7]
ult = list [-1]
resto = list[:-1]
tsil = [ult] + resto
for i in tsil:
    print(i)'''
#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
#semana. 
#• Calcular el promedio de las mínimas y el de las máximas. 
#• Mostrar en qué día se registró la mayor amplitud térmica.
