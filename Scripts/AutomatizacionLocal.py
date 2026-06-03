import shutil
import subprocess
import os

# Directorios
dir_origen_malla = "/home/jose/Descargas/Salome/Cuarto"
dir_destino_run = "/home/jose/OpenFOAM/jose-13/run/tutorials/fluid/Simulaciones/20k"
dir_polymesh = os.path.join(dir_destino_run, "constant", "polyMesh") 

# Archivos
nombre_malla = "20k.unv"
ruta_malla_origen = os.path.join(dir_origen_malla, nombre_malla)
ruta_malla_destino = os.path.join(dir_destino_run, nombre_malla)
ruta_archivo_boundary = os.path.join(dir_polymesh, "boundary")

print(f"Copiando '{nombre_malla}' a '{dir_destino_run}'...")
try:
    shutil.copy(ruta_malla_origen, ruta_malla_destino)
    print("Copia completada.")
except FileNotFoundError:
    print(f"Error: El archivo de origen '{ruta_malla_origen}' no fue encontrado.")
    exit()
except Exception as e:
    print(f"Error al copiar el archivo: {e}")
    exit()

# --- 3. Ejecutar ideasUnvToFoam ---
print(f"\n Ejecutando ideasUnvToFoam en '{dir_destino_run}'...")
try:
    # Cambiamos el directorio de trabajo para que el comando se ejecute correctamente
    # y los archivos de la malla (constant/polyMesh) se creen en el lugar correcto.
    resultado = subprocess.run(
        ["ideasUnvToFoam", nombre_malla],
        cwd=dir_destino_run, 
        check=True, 
        capture_output=True,
        text=True
    )
    print("ideasUnvToFoam ejecutado con éxito.")

except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar ideasUnvToFoam:")
    print(e.stderr)
    exit()
except FileNotFoundError:
    print("Error: 'ideasUnvToFoam' no se encontró. Asegúrate de que OpenFOAM esté configurado correctamente.")
    exit()

# --- 4. Modificar el Archivo boundary ---

# Nota: La ruta al archivo boundary es ahora:
# /home/jose/OpenFOAM/jose-13/run/tutorials/fluid/APP/constant/polyMesh/boundary
print(f"\n Modificando el archivo boundary en '{ruta_archivo_boundary}'...")

texto_buscar = "type" + 15 * " " + "patch;"
texto_reemplazar = "type" + 15 * " " + "wall;"

try:
    with open(ruta_archivo_boundary, "r") as archivo:
        contenido = archivo.read()

    nuevo_contenido = contenido.replace("type            patch;", "type            wall;")
    nuevo_contenido = nuevo_contenido.replace("type             patch;", "type             wall;")
    nuevo_contenido = nuevo_contenido.replace("type              patch;", "type              wall;")
    # ... y tu caso original
    nuevo_contenido = nuevo_contenido.replace("type                     patch;", "type                     wall;")     
    
    with open(ruta_archivo_boundary, "w") as archivo:
        archivo.write(nuevo_contenido)

    print("Modificación completada: 'patch' → 'wall' en el archivo boundary.")

except FileNotFoundError:
    print(f"Error: El archivo boundary '{ruta_archivo_boundary}' no fue encontrado.")
except Exception as e:
    print(f"Error al modificar el archivo boundary: {e}")

# --- 5. Fin del Script ---
print("\n El proceso de preparación de la malla ha finalizado.")
