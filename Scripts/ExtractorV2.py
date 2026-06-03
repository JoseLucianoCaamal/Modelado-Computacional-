from paraview.simple import *
import os
import re
import math

# --- Configuración de rutas ---
ruta_carpeta = "/home/jose/Documentos/Octave/Chimenea"
if not os.path.exists(ruta_carpeta):
    os.makedirs(ruta_carpeta)

# --- Menú de selección ---
print("\n--- Selector de Extracción ---")
print("1. Solo T (Temperatura)")
print("2. Solo U (Magnitud de Velocidad)")
print("3. Ambos (T y U)")
opcion = input("Elige una opción (1, 2 o 3): ").strip()

# Definimos qué vamos a buscar según la opción
variables_a_buscar = []
if opcion == "1":
    variables_a_buscar = ["T"]
elif opcion == "2":
    variables_a_buscar = ["U"]
elif opcion == "3":
    variables_a_buscar = ["T", "U"]
else:
    print("Opción no válida.")
    variables_a_buscar = []

def obtener_valor(p_data, nombre_var):
    arr = p_data.GetArray(nombre_var)
    if not arr:
        return None
    
    num_comp = arr.GetNumberOfComponents()
    if num_comp == 1:
        return arr.GetValue(0)
    else:
        # Si es vector (como U), calculamos magnitud
        v = [arr.GetComponent(0, i) for i in range(num_comp)]
        return math.sqrt(sum(c**2 for c in v))

# Diccionario para almacenar listas de datos dinámicamente
resultados = {var: [] for var in variables_a_buscar}

fuentes = GetSources()

# 1. Extracción de datos
for (nombre, id), proxy in fuentes.items():
    if "IntegrateVariables" in nombre:
        proxy.UpdatePipeline()
        datos = servermanager.Fetch(proxy)
        p_data = datos.GetPointData()
        
        for var in variables_a_buscar:
            valor = obtener_valor(p_data, var)
            if valor is not None:
                resultados[var].append((nombre, valor))

# 2. Función de ordenamiento natural
def natural_sort_key(item):
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', item[0])]

# 3. Ordenar y escribir archivos
for var, lista_datos in resultados.items():
    if lista_datos:
        lista_datos.sort(key=natural_sort_key)
        
        # Nombre de archivo dinámico
        nombre_file = "T.txt" if var == "T" else "U.txt"
        ruta_completa = os.path.join(ruta_carpeta, nombre_file)
        
        with open(ruta_completa, "w") as f:
            for n, v in lista_datos:
                f.write(f"{v:.7f}\n")
        
        print(f"Archivo generado: {nombre_file} con {len(lista_datos)} valores.")
    else:
        if variables_a_buscar:
            print(f"No se encontraron datos para la variable: {var}")

print("--- Proceso finalizado ---")