# Modelado Computacional de Tecnologías de Climatización Sustentable

Este repositorio contiene los recursos digitales, scripts de automatización y resultados de simulaciones transitorias desarrollados para la tesis de Ingeniería en Computación de la **Universidad Autónoma de Yucatán**.

El proyecto se enfoca en el análisis fluidodinámico y térmico de un sistema híbrido pasivo compuesto por un intercambiador de calor tierra-aire (EAHE) y chimeneas solares.

## Autores y Supervisión
* **Autor:** José Luciano Caamal Ayala
* **Directores de Tesis:**
  * Dr. Juan Manuel Rivero Fernández 
  * Dr. Johan Jair Estrada López
* **Institución:** Facultad de Matemáticas, UADY

---

## Animaciones de Simulaciones Dinámicas
Debido a la alta resolución de las mallas y la complejidad de los resultados transitorios, las animaciones completas se encuentran alojadas en un repositorio externo para garantizar la fluidez de la visualización.

| Caso de Estudio | Geometría Analizada | Enlace de Visualización|
| :--- | :--- | :--- |
| **Geometría 1** | Configuración base (EAHE + Chimenea única) | [Ver Simulación](https://1drv.ms/v/c/3f9252fb099dfb89/IQCQAck2W957TIqoWTPanITjAVvd6zC228OLwo4brht7NE4?e=XLchH8) |
| **Geometría 2** | Configuración de doble chimenea en paralelo | [Ver Simulación](https://1drv.ms/v/c/3f9252fb099dfb89/IQBxbMkUrInHR5eeZZUXRGDQAYGeDaCmMfTu3HheQvzpPjs?e=b8L2Zg) |
| **Geometría 3** | Configuración con chimenea de diámetro ampliado | [Ver Simulación](https://1drv.ms/v/c/3f9252fb099dfb89/IQAWekhCO_-ZRY1VaBISJCnOAQS1A4dn0ygKSu3jJbDg_rw?e=hTFQqs) |

---

## Herramientas Utilizadas
* **OpenFOAM v13:** Resolución de ecuaciones mediante volúmenes finitos.
* **SALOME:** Pre-procesamiento, diseño CAD y discretización del dominio (mallado).
* **Python (LINX):** Software de optimización y automatización desarrollado para la gestión de casos y notificaciones.
* **Paraview:** Post-procesamiento y análisis cualitativo de campos de presión y temperatura.

---

## 📂 Herramientas y Scripts de Automatización
Se han desarrollado herramientas específicas para optimizar el flujo de trabajo entre el mallado, la simulación y el análisis de datos:

### [LINX | OpenFOAM Engineering Dashboard (LINX.py)](LINX.py)
Interfaz gráfica integral para la gestión de casos. Permite automatizar el pre-procesamiento (`ideasUnvToFoam`, `checkMesh`), controlar la descomposición de mallas para paralelo y monitorear la ejecución de solvers en tiempo real.

### [Gestión de Flujo Local (AutomatizacionLocal.py)](AutomatizacionLocal.py)
Script de automatización secuencial para entornos locales. Realiza la conversión de malla, aplica la corrección de condiciones de frontera (cambio de `patch` a `wall`) y gestiona la pre-compilación de condiciones `coded` antes de lanzar la ejecución en paralelo.

### [Extractor de Datos de ParaView (ExtractorDeDatos.py)](ExtractorDeDatos.py)
Script de post-procesamiento masivo que interactúa con el núcleo de ParaView. Extrae magnitudes de Temperatura y Velocidad, utilizando un sistema de ordenamiento natural para facilitar el análisis cuantitativo posterior en Octave o MATLAB.

---

## Resumen Técnico
El sistema utiliza la **aproximación de Boussinesq** para modelar la convección natural impulsada por gradientes térmicos. Se validó la capacidad cuantitativa de OpenFOAM mediante la comparación con un modelo semi-analítico, logrando un error marginal de apenas **1.5%** en mallas de alta densidad (842,269 elementos).

---
*Este trabajo fue apoyado por la DGAPA de la UNAM por medio de la beca para titulación en el proyecto IA100225 PAPIIT.*
