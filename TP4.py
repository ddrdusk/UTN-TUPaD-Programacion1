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
