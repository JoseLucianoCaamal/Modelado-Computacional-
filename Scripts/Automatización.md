# 🛠️ Suite de Automatización y Software LINX para OpenFOAM

Este repositorio contiene las herramientas de software y scripts desarrollados para la gestión, ejecución y extracción de datos de simulaciones de climatización sustentable. La suite se divide en el software de gestión integral (LINX) y scripts especializados para tareas locales y post-procesamiento.

---

## 🚀 LINX | OpenFOAM Engineering Dashboard (`main.py`)

**LINX** es una interfaz gráfica de usuario (GUI) desarrollada en Python (Tkinter) diseñada para centralizar el flujo de trabajo de ingeniería en OpenFOAM. Permite gestionar simulaciones complejas sin necesidad de interactuar constantemente con la terminal de Linux.

### Características Principales:
* **Gestión de Casos:** Interfaz para navegar y seleccionar directorios de simulación.
* **Pre-procesamiento:** Automatización de comandos como `ideasUnvToFoam`, `checkMesh` y `setFields`.
* **Control de Paralelismo:** Configuración dinámica del archivo `decomposeParDict` y ejecución de `decomposePar`.
* **Monitoreo en Tiempo Real:** Terminal integrada para visualizar logs de ejecución (`foamRun`, `reconstructPar`, etc.).
* **Integración de Notificaciones:** Sistema de alertas para informar la finalización de procesos largos.

---

## 🐍 Scripts de Automatización Local

### 1. Gestión de Flujo de Trabajo (`code2.py`)
Este script está diseñado para la ejecución secuencial y automatizada en un entorno local, optimizando el tiempo entre la generación de la malla y el inicio del cálculo.
* **Conversión de Malla:** Transforma mallas de IDEAS (`.unv`) al formato nativo de OpenFOAM.
* **Corrección de Fronteras:** Automatiza la edición del archivo `constant/polyMesh/boundary` para cambiar parches (`patch`) a paredes (`wall`).
* **Compilación Dinámica:** Realiza una ejecución breve en serie para compilar condiciones `coded` antes de la descomposición.
* **Ejecución en Paralelo:** Configura y lanza la simulación utilizando `mpirun -np 8`.

### 2. Extracción de Datos de ParaView (`ExtractorV2.py`)
Script especializado para interactuar con el núcleo de ParaView y extraer información cuantitativa de manera masiva.
* **Filtrado de Variables:** Permite seleccionar la extracción de Temperatura (T), Magnitud de Velocidad (U) o ambas.
* **Integración Espacial:** Busca filtros de `IntegrateVariables` dentro del pipeline de ParaView.
* **Ordenamiento Natural:** Los datos extraídos se guardan en archivos `.txt` ordenados numéricamente (evitando el error de ordenamiento 1, 10, 2).
* **Exportación Directa:** Genera archivos listos para ser procesados en Octave o MATLAB.

---

## 🛠️ Requisitos del Sistema
* **Python 3.x** (Bibliotecas: `tkinter`, `PIL`, `paraview.simple`).
* **OpenFOAM** (Probado en versiones recientes como v13 o ESI-OpenCFD).
* **ParaView** con soporte para Python scripting.

---
*Desarrollado por José Luciano Caamal Ayala como parte del proyecto de tesis en la UADY.*
