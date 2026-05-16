# Trabajo Práctico N°2 – Gestión colaborativa

## Descripción general

Este repositorio corresponde al Trabajo Práctico N°2 de la asignatura **Organización Empresarial** de la Tecnicatura Universitaria en Programación (modalidad a distancia). El objetivo es integrar herramientas de gestión colaborativa y control de versiones (**Jira**, **Git**, **GitHub** y **Google Colab**) en el desarrollo de un pequeño proyecto de análisis de datos, respetando buenas prácticas de trazabilidad, documentación y trabajo en equipo.  

El proyecto se organiza siguiendo el enfoque de una célula de desarrollo con tres roles (Hugo, Paco y Luis). En este caso, los tres roles son ejecutados por un único estudiante, manteniendo igualmente la separación de responsabilidades y la documentación asociada a cada rol.

## Escenario elegido – Análisis de ventas (Escenario B)

El trabajo se basa en el **Escenario B – Análisis de Ventas de una pequeña empresa**, utilizando datos simulados de ventas de una empresa ficticia. El dataset incluye registros de distintos productos, cantidades vendidas, precios unitarios y fechas de venta.  

A partir de esta información se calculan indicadores básicos de desempeño comercial, tales como:

- Ventas totales en el período analizado.  
- Producto más vendido (por volumen de unidades).  
- Ventas agregadas por mes.  

Además, se genera al menos un **gráfico de la evolución de las ventas en el tiempo**, que se guarda en la carpeta de resultados.

## Roles y responsabilidades

El proyecto sigue la estructura de roles propuesta en la consigna:

- **P1 – Hugo (Líder y Organizador)**  
  Responsable de la creación del repositorio central en GitHub, la definición de la estructura inicial de carpetas (`datos/`, `scripts/`, `resultados/`) y la redacción del archivo `README.md` con la visión general del proyecto.

- **P2 – Paco (Desarrollador Técnico)**  
  Encargado de implementar en **Python** el script de análisis de ventas, asegurando que los datos se lean correctamente desde la carpeta `datos/`, que los indicadores se calculen de forma reproducible y que los resultados (tablas, métricas y gráficos) se almacenen en la carpeta `resultados/`.

- **P3 – Luis (Revisor y QA)**  
  Responsable de la revisión del código, la mejora de la documentación interna (comentarios técnicos), la configuración del archivo `.gitignore`, la verificación de que no se expongan datos sensibles ni credenciales, y la gestión de **Pull Requests** y comentarios técnicos antes del merge final.

> Nota: Los tres roles (P1, P2 y P3) son ejecutados por un único estudiante, manteniendo la separación de tareas y la trazabilidad entre Jira y GitHub.

## Dataset utilizado

El análisis se realiza a partir del archivo `data_ventas.csv`, almacenado en la carpeta `datos/` del repositorio. Este dataset corresponde a una empresa ficticia de productos tecnológicos e incluye las siguientes columnas principales:

- `producto`: nombre del producto vendido (por ejemplo, “Teclado Mecánico”, “Monitor 24 Pulgadas”, “Silla Ergonómica”, etc.).  
- `cantidad_vendida`: número de unidades vendidas en cada registro.  
- `precio`: precio unitario del producto en la moneda definida para el ejercicio.  
- `fecha_venta`: fecha en la que se registró la venta (formato año-mes-día).

A partir de estas columnas se calculan métricas como el monto de venta por registro, las ventas totales en el período, el producto más vendido y las ventas agregadas por mes.

## Estructura del repositorio

La estructura básica del repositorio sigue las recomendaciones de la cátedra para proyectos de análisis de datos:

- `datos/`  
  Contiene los archivos de datos utilizados en el análisis, en este caso `data_ventas.csv`. Se recomienda que los datasets estén en formato CSV para facilitar su lectura desde Python.

- `scripts/`  
  Incluye los scripts desarrollados en Python para el análisis de ventas. El código debe incorporar comentarios técnicos que expliquen la lógica aplicada en cada etapa (carga de datos, procesamiento, cálculos y generación de gráficos).

- `resultados/`  
  Almacena los resultados generados por el análisis, como gráficos de la evolución de las ventas, tablas exportadas u otros archivos derivados.

- `README.md`  
  Documento principal de descripción del proyecto, que resume el objetivo del trabajo, el escenario elegido, el dataset utilizado, la estructura del repositorio, los roles y las instrucciones para ejecutar el análisis.

- `.gitignore`  
  Archivo de configuración para excluir del control de versiones archivos y carpetas innecesarios o sensibles (por ejemplo, `__pycache__/`, `.ipynb_checkpoints/`, archivos temporales, logs, etc.).

## Tecnologías y herramientas

En este trabajo se utilizan las siguientes tecnologías y herramientas:

- **Python** como lenguaje principal de programación para el análisis de datos.  
- **Google Colab** como entorno de ejecución para los scripts de Python, aprovechando su integración con Git.  
- **Git** como sistema de control de versiones distribuido.  
- **GitHub** como repositorio remoto central para el proyecto y para la gestión de ramas y Pull Requests.  
- **Jira** como herramienta de gestión de tareas, utilizando épicas, historias de usuario, tareas y subtareas para organizar el trabajo y mantener la trazabilidad.

## Gestión del proyecto y trazabilidad

La planificación y el seguimiento del trabajo se realizan en **Jira**, donde se configura:

- Una **épica** que representa el Trabajo Práctico N°2 – Gestión colaborativa.  
- Tres **historias de usuario**, una para cada rol (P1, P2 y P3), con sus tareas y subtareas correspondientes.  
- Un flujo de trabajo basado en estados como **To Do**, **In Progress** y **Done**, que se actualizan a medida que avanza el proyecto.

Para mantener la trazabilidad entre Jira y GitHub, los mensajes de commit en Git siguen el mandato de la consigna: cada commit comienza con el **ID del issue de Jira** correspondiente (por ejemplo, `PROY-1: descripción del cambio`), lo que permite relacionar las tareas planificadas con los cambios concretos en el código.

## Instrucciones básicas de ejecución

1. Clonar este repositorio en el entorno local o abrirlo desde **Google Colab**.  
2. Verificar que el archivo `data_ventas.csv` se encuentre en la carpeta `datos/`.  
3. Abrir el script de análisis ubicado en la carpeta `scripts/` (por ejemplo, `analisis_ventas.py` o el notebook correspondiente).  
4. Ejecutar el script en Google Colab para:  
   - Cargar el dataset de ventas.  
   - Calcular los indicadores (ventas totales, producto más vendido, ventas por mes).  
   - Generar y guardar los gráficos y resultados en la carpeta `resultados/`.  

5. Revisar los resultados generados (archivos y gráficos) y, en caso de ser necesario, ajustar el código según los comentarios registrados en Jira y en los Pull Requests de GitHub.
