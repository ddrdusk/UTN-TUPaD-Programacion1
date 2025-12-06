import csv

# Función para leer los datos desde un archivo CSV
def leer_paises():
    paises = []
    try:
        with open('paises.csv', mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                paises.append({
                    'nombre': fila['nombre'],
                    'poblacion': int(fila['poblacion']),
                    'superficie': int(fila['superficie']),
                    'continente': fila['continente']
                })
    except FileNotFoundError:
        pass
    return paises

# Función para guardar los datos en el archivo CSV
def guardar_paises(paises):
    with open('paises.csv', mode='w', newline='', encoding='utf-8') as archivo:
        campos = ['nombre', 'poblacion', 'superficie', 'continente']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)

# Función para pedir un entero con manejo de errores
def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Error: debe ingresar un número válido.")

# Función para agregar un país
def agregar_pais(paises):
    nombre = input('Ingrese el nombre del país: ').strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    if any(p['nombre'].lower() == nombre.lower() for p in paises):
        print("El país ya existe en la base de datos.")
        return
    
    poblacion = pedir_entero('Ingrese la población del país: ')
    superficie = pedir_entero('Ingrese la superficie en km² del país: ')
    continente = input('Ingrese el continente del país: ').strip().capitalize()
    
    pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    paises.append(pais)
    guardar_paises(paises)
    print("País agregado correctamente.")

# Función para actualizar datos de un país
def actualizar_pais(paises):
    nombre = input('Ingrese el nombre del país a actualizar: ').strip()
    for pais in paises:
        if nombre.lower() == pais['nombre'].lower():
            print(f"Datos actuales de {pais['nombre']}: Población = {pais['poblacion']}, Superficie = {pais['superficie']}")
            nueva_poblacion = pedir_entero('Ingrese la nueva población: ')
            nueva_superficie = pedir_entero('Ingrese la nueva superficie: ')
            pais['poblacion'] = nueva_poblacion
            pais['superficie'] = nueva_superficie
            guardar_paises(paises)
            print("Datos actualizados correctamente.")
            return
    print("No se encontró el país.")

# Función para buscar un país por nombre (coincidencia parcial)
def buscar_pais(paises):
    nombre = input('Ingrese el nombre del país a buscar: ').strip()
    resultados = [pais for pais in paises if nombre.lower() in pais['nombre'].lower()]
    if resultados:
        for pais in resultados:
            mostrar_pais(pais)
    else:
        print("No se encontraron países con ese nombre.")

# Función para filtrar países por continente
def filtrar_por_continente(paises):
    continente = input('Ingrese el continente: ').strip().capitalize()
    resultados = [pais for pais in paises if continente in pais['continente']]
    if resultados:
        for pais in resultados:
            mostrar_pais(pais)
    else:
        print(f"No se encontraron países en el continente {continente}.")

# Función para filtrar países por rango de población
def filtrar_por_rango_poblacion(paises):
    min_poblacion = pedir_entero('Ingrese la población mínima: ')
    max_poblacion = pedir_entero('Ingrese la población máxima: ')
    resultados = [pais for pais in paises if min_poblacion <= pais['poblacion'] <= max_poblacion]
    if resultados:
        for pais in resultados:
            mostrar_pais(pais)
    else:
        print(f"No se encontraron países en el rango de población de {min_poblacion} a {max_poblacion}.")

# Función para filtrar países por rango de superficie
def filtrar_por_rango_superficie(paises):
    min_superficie = pedir_entero('Ingrese la superficie mínima en km²: ')
    max_superficie = pedir_entero('Ingrese la superficie máxima en km²: ')
    resultados = [pais for pais in paises if min_superficie <= pais['superficie'] <= max_superficie]
    if resultados:
        for pais in resultados:
            mostrar_pais(pais)
    else:
        print(f"No se encontraron países en el rango de superficie de {min_superficie} a {max_superficie} km².")

# Función para ordenar países
def ordenar_paises(paises):
    criterio = input('¿Cómo desea ordenar? (nombre/poblacion/superficie): ').strip().lower()
    orden = input('¿Orden ascendente o descendente? (asc/desc): ').strip().lower()

    if criterio == 'nombre':
        paises.sort(key=lambda pais: pais['nombre'], reverse=(orden == 'desc'))
    elif criterio == 'poblacion':
        paises.sort(key=lambda pais: pais['poblacion'], reverse=(orden == 'desc'))
    elif criterio == 'superficie':
        paises.sort(key=lambda pais: pais['superficie'], reverse=(orden == 'desc'))
    else:
        print("Criterio de ordenamiento no válido.")
        return

    for pais in paises:
        mostrar_pais(pais)

# Función para mostrar estadísticas
def mostrar_estadisticas(paises):
    if not paises:
        print("No hay países registrados.")
        return

    mayor_poblacion = max(paises, key=lambda pais: pais['poblacion'])
    menor_poblacion = min(paises, key=lambda pais: pais['poblacion'])
    promedio_poblacion = sum(pais['poblacion'] for pais in paises) / len(paises)
    promedio_superficie = sum(pais['superficie'] for pais in paises) / len(paises)

    print(f"País con mayor población: {mayor_poblacion['nombre']} ({mayor_poblacion['poblacion']})")
    print(f"País con menor población: {menor_poblacion['nombre']} ({menor_poblacion['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")

    continentes = {}
    for pais in paises:
        if pais['continente'] not in continentes:
            continentes[pais['continente']] = 1
        else:
            continentes[pais['continente']] += 1

    for continente, cantidad in continentes.items():
        print(f"Cantidad de países en {continente}: {cantidad}")

# Función para mostrar un país de forma legible
def mostrar_pais(pais):
    print(f"{pais['nombre']:<15}  Pob: {pais['poblacion']:<10}  Sup: {pais['superficie']:<10}  Cont: {pais['continente']}")

# Función para mostrar el menú
def mostrar_menu():
    print("\n----- Menú de opciones -----")
    print("1. Agregar un país")
    print("2. Actualizar datos de un país")
    print("3. Buscar un país")
    print("4. Filtrar países por continente")
    print("5. Filtrar países por rango de población")
    print("6. Filtrar países por rango de superficie")
    print("7. Ordenar países")
    print("8. Mostrar estadísticas")
    print("9. Salir")

def main():
    paises = leer_paises()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            agregar_pais(paises)
        elif opcion == '2':
            actualizar_pais(paises)
        elif opcion == '3':
            buscar_pais(paises)
        elif opcion == '4':
            filtrar_por_continente(paises)
        elif opcion == '5':
            filtrar_por_rango_poblacion(paises)
        elif opcion == '6':
            filtrar_por_rango_superficie(paises)
        elif opcion == '7':
            ordenar_paises(paises)
        elif opcion == '8':
            mostrar_estadisticas(paises)
        elif opcion == '9':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
