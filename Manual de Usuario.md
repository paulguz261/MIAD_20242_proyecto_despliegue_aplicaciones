
# Manual de Usuario: Tablero de Predicción de Riesgo de Accidentes Cerebrovasculares (ACV)

---

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Objetivo del Tablero](#objetivo-del-tablero)
3. [Requisitos Previos](#requisitos-previos)
4. [Descripción de Funcionalidades](#descripción-de-funcionalidades)
   - [Carga de Datos](#carga-de-datos)
   - [Ingreso de Variables](#ingreso-de-variables)
   - [Interpretación de Resultados](#interpretación-de-resultados)
5. [Instrucciones de Uso](#instrucciones-de-uso)
   - [Inicio del Tablero](#inicio-del-tablero)
   - [Navegación en la Interfaz](#navegación-en-la-interfaz)
   - [Lectura del Gráfico de Gauge](#lectura-del-gráfico-de-gauge)
6. [Ejemplo de Caso de Uso](#ejemplo-de-caso-de-uso)
7. [Solución de Problemas Comunes](#solución-de-problemas-comunes)
8. [Glosario de Términos](#glosario-de-términos)
9. [Contacto y Soporte Técnico](#contacto-y-soporte-técnico)
10. [Licencia y Colaboración](#licencia-y-colaboración)

---

## Introducción
El tablero de predicción de riesgo de accidentes cerebrovasculares (ACV) es una herramienta interactiva desarrollada en **Dash de Plotly**. Permite calcular la probabilidad de riesgo de ACV basándose en características clínicas y demográficas, presentando resultados claros y visuales.

---

## Objetivo del Tablero
El objetivo es proporcionar a profesionales de la salud una herramienta rápida y precisa para estimar el riesgo de ACV, apoyando la toma de decisiones médicas y la prevención proactiva.

---

## Requisitos Previos
Antes de utilizar el tablero, asegúrate de contar con lo siguiente:
- **Python 3.7+** instalado.
- Librerías requeridas: `dash`, `dash-bootstrap-components`, `plotly`, `pandas`, etc.
- Un archivo CSV o entrada de datos clínicos como:
  - Edad
  - Género
  - Hipertensión
  - Enfermedades cardíacas
  - Tipo de trabajo
  - Estado civil
  - Tipo de residencia
  - Glucosa en sangre
  - IMC
  - Estado de fumador

Para instalar las dependencias, ejecuta:
```bash
pip install dash dash-bootstrap-components plotly pandas
```

---

## Descripción de Funcionalidades

### Carga de Datos
- Permite ingresar datos manualmente a través de la interfaz.

### Ingreso de Variables
Cada campo en la interfaz corresponde a una variable importante:
1. **Género**: Masculino o Femenino.
2. **Edad**: En años.
3. **Hipertensión**: 0 (No) o 1 (Sí).
4. **Enfermedades Cardíacas**: 0 (No) o 1 (Sí).
5. **Tipo de Trabajo**: Selección de categorías predefinidas.
6. **Estado Civil**: Casado o Soltero.
7. **Tipo de Residencia**: Urbana o Rural.
8. **Nivel de Glucosa en Sangre**: En mg/dL.
9. **IMC (Índice de Masa Corporal)**: En kg/m².
10. **Estado de Fumador**: Fumador, Exfumador o Nunca Fumador.

### Interpretación de Resultados
- El resultado se presenta en un gráfico de **gauge**, con los siguientes rangos:
  - **Zona Verde**: Bajo riesgo (0-30%).
  - **Zona Amarilla**: Riesgo moderado (30-70%).
  - **Zona Roja**: Alto riesgo (>70%).

---

## Instrucciones de Uso

### Inicio del Tablero
1. Clona el repositorio:
   ```bash
   git clone https://github.com/paulguz261/MIAD_20242_proyecto_despliegue_aplicaciones
   ```
2. Navega al directorio:
   ```bash
   cd MIAD_20242_proyecto_despliegue_aplicaciones
   cd code
   cd dash
   ```
3. Ejecuta el tablero:
   ```bash
   python app.py
   ```
4. Abre tu navegador y accede a: [http://127.0.0.1:8050/](http://127.0.0.1:8050/).

### Navegación en la Interfaz
1. Ingresa los valores en los campos correspondientes.
2. Haz clic en el botón **"Calcular Riesgo"**.
3. Observa el gráfico de gauge y analiza el riesgo.

### Lectura del Gráfico de Gauge
- El puntero indica el nivel de riesgo.
- Los colores ayudan a identificar rápidamente el nivel:
  - Verde: Bajo.
  - Amarillo: Moderado.
  - Rojo: Alto.

---

## Ejemplo de Caso de Uso
1. Datos ingresados:
   - Género: Femenino
   - Edad: 65
   - Hipertensión: Sí
   - Enfermedades Cardíacas: No
   - Tipo de Trabajo: Retirado
   - Nivel de Glucosa: 140 mg/dL
   - IMC: 28
   - Fumador: Nunca Fumador
2. Resultado:
   - **Gráfico de Gauge**: 75% (Zona Roja).
   - Interpretación: Riesgo alto, recomendar evaluación médica inmediata.

---

## Solución de Problemas Comunes

### El tablero no carga
1. Verifica que Python esté instalado correctamente.
2. Asegúrate de haber instalado todas las dependencias.

### Error en el ingreso de datos
- Confirma que los valores están dentro de los rangos esperados (edad positiva, glucosa razonable, etc.).

---

## Glosario de Términos
- **ACV (Accidente Cerebrovascular)**: Interrupción del flujo de sangre al cerebro.
- **IMC (Índice de Masa Corporal)**: Indicador de peso saludable.
- **Glucosa en sangre**: Nivel de azúcar en la sangre.

---

## Contacto y Soporte Técnico
Si encuentras problemas o tienes preguntas, contacta:
- **Correo electrónico**: jc.acosta12@uniandes.edu.co
- **GitHub**: [juanacosta5](https://github.com/paulguz261/MIAD_20242_proyecto_despliegue_aplicaciones)

- **Correo electrónico**: sk.olaya@uniandes.edu.co
- **GitHub**: [soniakolaya](https://github.com/paulguz261/MIAD_20242_proyecto_despliegue_aplicaciones)

- **Correo electrónico**: ps.guzman150@uniandes.edu.co
- **GitHub**: [paulguz261](https://github.com/paulguz261/MIAD_20242_proyecto_despliegue_aplicaciones)

- **Correo electrónico**: ns.posada@uniandes.edu.co
- **GitHub**: [nasly-posada](https://github.com/paulguz261/MIAD_20242_proyecto_despliegue_aplicaciones)
---

## Licencia y Colaboración
Este proyecto está licenciado bajo la Universidad de los Andes, en la maestría de inteligencia analítica de datos (MIAD). Se aceptan contribuciones; por favor, abre un [issue] o un pull request en GitHub.
