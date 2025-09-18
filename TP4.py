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
'''from statistics import mean
temps = [
    [1 , 15],
    [10 , 23],
    [40 , 41],
    [-3 , 33],
    [15 , 15],
    [9 , 23],
    [16 , 19]
]
mins = []
maxs = []
for i in temps:
    mins.append(min(i))
    maxs.append(max(i))
print(f"Promedio de minimas: {mean(mins)}")
print(f"Promedio de minimas: {mean(maxs)}")
amptemp = [i[1] - i[0] for i in temps]
maxamp = amptemp.index(max(amptemp)) + 1
print(f"el dia de mayor amplitud fue: {maxamp}")'''
#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia. 
'''from statistics import mean
nots = [
    [1 , 10 , 10],
    [10 , 3 , 9],
    [4 , 1 , 8],
    [3 , 3 , 7],
    [1 , 5 , 6],
]
estudiante = 0
mate = []
mlengua = []
mciencia = []
for i in nots:
    estu =+ 1
    print(f"promedio del estudiane {nots.index(i) + 1}: {mean(i)}")
    mate.append(i[0])
    mlengua.append(i[1])
    mciencia.append(i[2])
print(f"Promedio de Matematica: {mean(mate)}")
print(f"Promedio de Lengua: {mean(mlengua)}")
print(f"Promedio de Ciencia: {mean(mciencia)}")'''
#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#• Mostrar el tablero después de cada jugada. 
'''tate = [
    ["-" , "-" , "-"],
    ["-" , "-" , "-"],
    ["-" , "-" , "-"]
]
for i in range(9):
    print(tate)
    p1f = int(input("P1, ingrese n° fila ")) - 1
    p1c = int(input("P1, ingrese n° columna ")) - 1
    tate[p1f][p1c] = "x"
    print(tate)
    p2f = int(input("P2, ingrese fila ")) + 1
    p2c = int(input("P2, ingrese columna ")) + 1
    tate[p2f][p2c] = "O"'''
#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana.
'''prod = [
    [1 , 15 , 35 , 18 , 21 , 54 , 47],
    [10 , 23 , 8 , 74 , 21 , 54 , 47],
    [40 , 41 , 38 , 83 , 21 , 54 , 47],
    [3 , 33 , 18 , 93 , 21 , 54 , 47]
]
tot = []
for i in range(4):
    totprod = 0
    for j in range(7):
        totprod += prod[i][j]
    tot.append(totprod)
    print(f"Total del producto {i + 1}: {totprod}")
#2da parte
maxdia = 0
maxvent = 0
for j in range(7):
    totdia = 0
    for i in range(4):
        totdia += prod[i][j]
    if totdia > maxvent:
        maxvent = totdia
        maxdia = j
print(f"El dia con las mayores fue el {maxdia + 1}°")
#3ra parte
print(tot.index(max(tot)) + 1)'''