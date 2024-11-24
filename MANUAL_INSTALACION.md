
# Manual de Instalación: Tablero de Predicción de Riesgo de Accidentes Cerebrovasculares (ACV)

---

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Preparación del Entorno](#preparación-del-entorno)
4. [Instalación Paso a Paso](#instalación-paso-a-paso)
5. [Prueba del Tablero](#prueba-del-tablero)
6. [Solución de Problemas](#solución-de-problemas)
7. [Contacto y Soporte Técnico](#contacto-y-soporte-técnico)

---

## Introducción
Este documento explica cómo instalar y ejecutar el tablero de predicción de riesgo de accidentes cerebrovasculares (ACV) en un entorno local.

---

## Requisitos del Sistema
1. **Sistema Operativo**: Windows, macOS o Linux.
2. **Python**: Versión 3.7 o superior.
3. **Librerías**:
   - `dash`
   - `plotly`
   - `dash-bootstrap-components`
   - `pandas`
4. **Hardware**:
   - Procesador: Dual-core o superior.
   - RAM: 4 GB o más.

---

## Preparación del Entorno
1. **Instalar Python**:
   - Descarga Python desde [python.org](https://www.python.org/downloads/) e instálalo.
2. **Instalar Git** (opcional):
   - Si vas a clonar el repositorio, instala Git desde [git-scm.com](https://git-scm.com/).

---

## Instalación Paso a Paso
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

---

## Prueba del Tablero
1. Ejecuta el archivo principal del tablero:
   ```bash
   python app.py
   ```
2. Abre tu navegador y accede a:
   [http://127.0.0.1:8050/](http://127.0.0.1:8050/)

---

## Solución de Problemas
1. **El tablero no carga**:
   - Verifica que Python esté instalado.
   - Confirma que las dependencias están correctamente instaladas.
2. **Error de versión de Python**:
   - Usa `python --version` para confirmar la versión.
3. **Problemas con dependencias**:
   - Ejecuta nuevamente: `pip install -r requirements.txt`.

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
