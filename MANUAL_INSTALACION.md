# Manual de Instalación: Tablero de Predicción de Riesgo de Accidentes Cerebrovasculares (ACV)

---

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Preparación del Entorno](#preparación-del-entorno)
4. [Instalación Paso a Paso](#instalación-paso-a-paso)
5. [Configuración en la Nube](#configuración-en-la-nube)
6. [Prueba del Tablero](#prueba-del-tablero)
7. [Solución de Problemas](#solución-de-problemas)
8. [Contacto y Soporte Técnico](#contacto-y-soporte-técnico)

---

## Introducción
Este documento detalla el proceso de instalación, configuración y ejecución del tablero de predicción de riesgo de accidentes cerebrovasculares (ACV). La solución incluye una API y un tablero Dash para la visualización de resultados.

---

## Requisitos del Sistema

### Local
1. **Sistema Operativo**: Windows, macOS o Linux.
2. **Python**: Versión 3.7 o superior.
3. **Librerías**:
   - `dash`
   - `plotly`
   - `dash-bootstrap-components`
   - `pandas`
   - `requests`
   - `xgboost`
4. **Hardware**:
   - Procesador: Dual-core o superior.
   - RAM: 4 GB o más.

### Nube
1. **Proveedor de la nube**: AWS (o equivalente).
2. **Configuración mínima de la máquina virtual**:
   - **CPU**: 2 vCPU.
   - **RAM**: 4 GB.
   - **Sistema Operativo**: Ubuntu 20.04 o superior.
   - **Puertos abiertos**:
     - API: 8000.
     - Tablero: 8050.

---

## Preparación del Entorno

1. **Instalar Python**:
   - Descarga Python desde [python.org](https://www.python.org/downloads/) e instálalo.
2. **Instalar Git** (opcional):
   - Si vas a clonar el repositorio, instala Git desde [git-scm.com](https://git-scm.com/).

---

## Instalación Paso a Paso

### En tu entorno local o máquina virtual:

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/paulguz261/MIAD_20242_proyecto_despliegue_aplicaciones
   ```
2. **Navegar al directorio del proyecto**:
   ```bash
   cd MIAD_20242_proyecto_despliegue_aplicaciones
   cd code
   cd dash
   ```
3. **Crear un entorno virtual** (opcional, pero recomendado):
   ```bash
   python -m venv env
   source env/bin/activate  # Para macOS/Linux
   env\Scripts\activate   # Para Windows
   ```
4. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Descargar y colocar el archivo model.pkl**:
   Descarga o genera el archivo model.pkl usando las instrucciones del código proporcionado en la documentación. 
   Colócalo en la ruta correspondiente del backend de la API.
---
### Configuración en la Nube:

1. **Configuración de la API**:
Subir el archivo model.pkl a la máquina virtual: Usa SCP o una herramienta de transferencia de archivos para cargar model.pkl
   ```bash
   scp model.pkl ubuntu@<ip-publica>:~/api_modelo/trained
   ```
2. **Iniciar API con Uvicorn**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
3. **Crear un entorno virtual** (opcional, pero recomendado):
   ```bash
   python -m venv env
   source env/bin/activate  # Para macOS/Linux
   env\Scripts\activate   # Para Windows
   ```
## Prueba del Tablero
1. Ejecuta el archivo principal del tablero:
   ```bash
   python app.py
   ```
2. Abre tu navegador y accede a:
   [http://<ip-publica>:8050/](http://<ip-publica>:8050/)

Realiza una predicción completando los campos y presionando el botón de predecir.

---

## Solución de Problemas
1. **El tablero no carga**:
   - Verifica que Python esté instalado.
   - Confirma que las dependencias están correctamente instaladas.
2. **Error de versión de Python**:
   - Usa `python --version` para confirmar la versión.
3. **Problemas con dependencias**:
   - Ejecuta nuevamente: `pip install -r requirements.txt`.
4. **Conflicto de puertos**:
   - Para deterner los procesos existentes: `sudo lsof -i :<puerto> sudo kill -9 <PID>`.
---

## Contacto y Soporte Técnico
Para cualquier problema o duda, contacta a:
- **Correo electrónico**: jc.acosta12@uniandes.edu.co
- **GitHub**: [juanacosta5](https://github.com/paulguz261/MIAD_20242_proyecto_despliegue_aplicaciones)

- **Correo electrónico**: sk.olaya@uniandes.edu.co
- **GitHub**: [soniakolaya](https://github.com/paulguz261/MIAD_20242_proyecto_despliegue_aplicaciones)

- **Correo electrónico**: ps.guzman150@uniandes.edu.co
- **GitHub**: [paulguz261](https://github.com/paulguz261/MIAD_20242_proyecto_despliegue_aplicaciones)

- **Correo electrónico**: ns.posada@uniandes.edu.co
- **GitHub**: [nasly-posada](https://github.com/paulguz261/MIAD_20242_proyecto_despliegue_aplicaciones)


