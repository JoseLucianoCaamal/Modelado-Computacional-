# Modelado Computacional de Tecnologias de Climatizacion Sustentable

Este repositorio contiene los recursos digitales, scripts de automatizacion y resultados de simulaciones transitorias desarrollados para la tesis de Ingenieria en Computacion de la Universidad Autonoma de Yucatan.

El proyecto se enfoca en el analisis fluidodinamico y termico de un sistema hibrido pasivo compuesto por un intercambiador de calor tierra-aire (EAHE) y chimeneas solares.

## Autores y Supervision
* Autor: Jose Luciano Caamal Ayala
* Directores de Tesis:
  * Dr. Juan Manuel Rivero Fernandez, ENES Merida, UNAM
  * Dr. Johan Jair Estrada Lopez, UADY
* Institucion: Facultad de Matematicas, UADY

---

## Animaciones de Simulaciones Dinamicas
Debido a la alta resolucion de las mallas y la complejidad de los resultados transitorios, las animaciones completas se encuentran alojadas en un repositorio externo para garantizar la fluidez de la visualizacion.

| Caso de Estudio | Geometria Analizada | Enlace de Visualizacion |
| :--- | :--- | :--- |
| Geometria 1 | Configuracion base (EAHE + Chimenea unica) | [Ver Simulacion](https://1drv.ms/v/c/3f9252fb099dfb89/IQCQAck2W957TIqoWTPanITjAVvd6zC228OLwo4brht7NE4?e=XLchH8) |
| Geometria 2 | Configuracion de doble chimenea en paralelo | [Ver Simulacion](https://1drv.ms/v/c/3f9252fb099dfb89/IQBxbMkUrInHR5eeZZUXRGDQAYGeDaCmMfTu3HheQvzpPjs?e=b8L2Zg) |
| Geometria 3 | Configuracion con chimenea de diametro ampliado | [Ver Simulacion](https://1drv.ms/v/c/3f9252fb099dfb89/IQAWekhCO_-ZRY1VaBISJCnOAQS1A4dn0ygKSu3jJbDg_rw?e=hTFQqs) |

---

## Herramientas Utilizadas
* OpenFOAM v13: Resolucion de ecuaciones mediante volumenes finitos.
* SALOME: Pre-procesamiento, diseño CAD y discretizacion del dominio (mallado).
* Python (LINX): Software de optimizacion y automatizacion desarrollado para la gestion de casos y notificaciones.
* Paraview: Post-procesamiento y analisis cualitativo de campos de presion y temperatura.

---

## Herramientas y Scripts de Automatizacion
Se han desarrollado herramientas especificas para optimizar el flujo de trabajo entre el mallado, la simulacion y el analisis de datos. Puede acceder al codigo fuente mediante los siguientes enlaces:

### [LINX | OpenFOAM Engineering Dashboard](Scripts/LINX)
Interfaz grafica integral para la gestion de casos de estudio. Automatiza procesos de pre-procesamiento como ideasUnvToFoam y checkMesh, permite configurar la descomposicion de dominios para calculo en paralelo y ofrece una terminal integrada para el monitoreo de los solvers.

### [Gestion de Flujo Local (AutomatizacionLocal.py)](Scripts/AutomatizacionLocal.py)
Script de automatizacion secuencial diseñado para ejecucion local. Gestiona la conversion de malla, la redefinicion de condiciones de frontera (sustitucion de patch por wall) y la compilacion previa de bibliotecas dinamicas (dynamicCode) antes de iniciar el procesamiento paralelo con mpirun.

### [Extractor de Datos de ParaView (ExtractorDeDatos.py)](Scripts/ExtractorDeDatos.py)
Script de post-procesamiento masivo que interactua con la API de ParaView. Realiza la extraccion automatizada de perfiles de Temperatura y Velocidad, implementando un sistema de ordenamiento natural para asegurar la integridad de los datos destinados a analisis numerico en Octave o MATLAB.

---

## Resumen Tecnico
El sistema utiliza la aproximacion de Boussinesq para modelar la conveccion natural impulsada por gradientes termicos. Se valido la capacidad cuantitativa de OpenFOAM mediante la comparacion con un modelo semi-analitico, logrando un error marginal de 1.5 por ciento en mallas de alta densidad (842,269 elementos).

---
*Este trabajo fue apoyado por la DGAPA de la UNAM por medio de la beca para titulacion en el proyecto IA100225 PAPIIT.*
