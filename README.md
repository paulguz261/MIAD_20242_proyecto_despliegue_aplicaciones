# Modelo Predictivo para Diagnóstico de Accidentes Cerebrovascular

Este repositorio contiene el codigo, datos y resultados del proyecto diseñado para predecir si una persona puede estar en riesgo de presentar un accidente cerebrovascular a partir del conjunto de datos [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/data). En su desarrollo se usaron ténicas de aprendizaje supervisado para predecir la probabilidad de una persona sufra un ACV dado unos factores de riesgo. El objetivo de este proyecto fue desarrollar y desplegar un producto de analitica de datos.


## Estructura de repositorio
El repositorio esta organizado en las siguientes carpetas:
- *data:* Contiene dos carpetas con los datos.
    - *raw_data:* Almacena los datos crudos descargados desde Kaggle.
    - *processed_data:* Contiene los datos procesados y transformados para aplicar análisis exploratorio de datos y preprocesamiento.
- *models:* Almacena los diferentes modelos predictivos entrenados.
- *documentation:* Contiene la documentación final del proyecto y diccionarios de los conjuntos de datos empleados.

## Como ejecutar el Código
1. Configurar el entorno de Python:

-   En Windows:

    a. Asegúrate de tener [Python](https://www.python.org/downloads/) instalado en tu sistema.

    b. Abre una terminal (Command Prompt o PowerShell) y navega al directorio del proyecto.

    c. Crea un entorno virtual con el siguiente comando:
    ```bash
    python -m venv env
    ```
    d. Activa el entorno virtual:
    ```bash
    .\env\Scripts\activate
    ```
- En macOS:

    a. Asegúrate de tener [Python](https://www.python.org/downloads/) instalado en tu sistema.

    b. Abre una terminal y navega al directorio del proyecto.

    c. Crea un entorno virtual con el siguiente comando:
    ```bash
        python3 -m venv env
    ```
    d. Activa el entorno virtual:
    ```bash
    source env/bin/activate
    ```
2. Instalar dependencias: Una vez que el entorno virtual esté activado, debes instalar las dependencias necesarias utilizando el archivo requirements.txt


```bash
pip install -r requirements.txt
```
## Contribucciones

¡Las contribucciones son siempre bienvenidas!

Si deseas contribuir al proyecto, abre un *issue* o envianos un *pull request* con tus propuestas. Asegúrate de seguir las mejores prácticas y documentar cualquier cambio a realizar.


## Autores

Para cualquier consulta relacionada con el proyecto, puedes contactar a cualquier integrante del equipo que desarrollo el proyecto.
- Nasly Posada: [ns.posada@uniandes.edu.co](ns.posada@uniandes.edu.co)
- Sonia Olaya: [sk.olaya@uniandes.edu.co](sk.olaya@uniandes.edu.co)
- Paul Guzman: [ps.guzman150@uniandes.edu.co](ps.guzman150@uniandes.edu.co)
- Juan Acosta: [jc.acosta12@uniandes.edu.co](jc.acosta12@uniandes.edu.co)