# Procedimiento para leer un archivo y almacenar las contraseñas en un arreglo de datos
def leer_archivo(archivo):
    contraseñas = []
    with open(archivo, 'r') as file:
        for line in file:
            contraseñas.append(line.strip())
    return contraseñas

# Procedimiento para calcular el puntaje de seguridad de una contraseña
def calcular_puntaje(contraseña):
    puntaje = len(contraseña)  # Por cada carácter que posea la contraseña, se suma 1 punto
    if any(c.islower() for c in contraseña):  # Si hay letras minúsculas, se suma 1 punto
        puntaje += 1
    if any(c.isdigit() for c in contraseña):  # Si hay números, se suma 1 punto
        puntaje += 1
    if any(c.isupper() for c in contraseña):  # Si hay letras mayúsculas, se suma 1 punto
        puntaje += 1
    if any(c in "!@#$%^&*()-_+=~`[]{}|:;,.<>?/" for c in contraseña):  # Si hay símbolos, se suman 3 puntos
        puntaje += 3
        puntaje += (contraseña.count("!@#$%^&*()-_+=~`[]{}|:;,.<>?/") - 1) * 2  # Por cada símbolo adicional al primero, se suman 2 puntos
    return puntaje

# Procedimiento para clasificar una contraseña según su puntaje de seguridad
def clasificar_contraseña(puntaje):
    if puntaje <= 15:
        return "Débil"
    elif puntaje <= 20:
        return "Moderada"
    elif puntaje <= 35:
        return "Buena"
    elif puntaje <= 100:
        return "Excelente"
    else:
        return "Impenetrable"

# Procedimiento para ordenar las contraseñas según su puntaje de seguridad utilizando el algoritmo de ordenamiento de burbujas
def ordenar_contraseñas(contraseñas):
    n = len(contraseñas)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if calcular_puntaje(contraseñas[j]) < calcular_puntaje(contraseñas[j + 1]):
                contraseñas[j], contraseñas[j + 1] = contraseñas[j + 1], contraseñas[j]

# Procedimiento para verificar si las contraseñas contenidas en el archivo de patrones están en el archivo de contraseñas y generar un archivo de coincidencias
def verificar_coincidencias(contraseñas, patrones, archivo_coincidencias):
    coincidencias = []
    for contraseña in contraseñas:
        if any(patron in contraseña for patron in patrones):
            coincidencias.append(contraseña)
    with open(archivo_coincidencias, 'w') as file:
        for contraseña in coincidencias:
            file.write(contraseña + "\n")

# Procedimiento para exportar las contraseñas, su categoría y puntaje de seguridad a un archivo en formato txt
def exportar_archivo(contraseñas, archivo_exportado):
    with open(archivo_exportado, 'w') as file:
        file.write("Contraseña | Categoría | Puntos de Seguridad\n")
        for contraseña in contraseñas:
            puntaje = calcular_puntaje(contraseña)
            categoría = clasificar_contraseña(puntaje)
            file.write(f"{contraseña} | {categoría} | {puntaje}\n")

# Leer el archivo de contraseñas y almacenar las contraseñas en un arreglo de datos
contraseñas = leer_archivo("contraseñas.txt")

# Leer el archivo de patrones y cargarlos a otro arreglo de datos
patrones = leer_archivo("patrones.txt")

# Calcular los puntos de seguridad de cada contraseña
puntajes = [calcular_puntaje(contraseña) for contraseña in contraseñas]

# Clasificar las contraseñas según sus puntos de seguridad
categorías = [clasificar_contraseña(puntaje) for puntaje in puntajes]

# Ordenar las contraseñas según sus puntos de seguridad de mayor a menor utilizando el algoritmo de ordenamiento de burbujas
ordenar_contraseñas(contraseñas)

# Verificar si las contraseñas contenidas en el archivo de patrones están en el archivo de contraseñas y generar un archivo de coincidencias
verificar_coincidencias(contraseñas, patrones, "coincidencias.txt")

# Exportar las contraseñas, su categoría y puntaje de seguridad a un archivo en formato txt
exportar_archivo(contraseñas, "exportado.txt")
