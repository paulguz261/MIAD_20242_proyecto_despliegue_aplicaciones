# ------------------------------------------------------------------------------------------------------
# ----------------------------------- Importación de librerías -----------------------------------------
# ------------------------------------------------------------------------------------------------------

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import requests

# Dirección de la API (reemplaza con la URL real de tu API)
API_URL = "http://54.147.211.102:8000/predict"

# ------------------------------------------------------------------------------------------------------
# -------------------------------------- Se inicializa Dash --------------------------------------------
# ------------------------------------------------------------------------------------------------------
app = dash.Dash(__name__)

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------- Diseño APP -----------------------------------------------
# ------------------------------------------------------------------------------------------------------
app.layout = html.Div(style={'font-family': 'Arial', 'backgroundColor': '#F0F4F8', 'padding': '20px'}, children=[
    html.H1("Modelo predictivo para Diagnóstico de Accidente Cerebrovascular", 
            style={'text-align': 'center', 'color': '#B71C1C', 'font-weight': 'bold'}),

    html.P("Herramienta que permite predecir la probabilidad de una persona sufra un ACV dado unos factores de riesgo. "
           "Por favor ingrese las siguientes variables, para predecir la probabilidad de estar en riesgo de padecer un ACV.", 
           style={'text-align': 'center', 'color': '#455A64'}),

    # Fila 1
    html.Div([
        # Género
        html.Div([
            html.Label("Género"),
            dcc.RadioItems(
                options=[
                    {'label': 'Mujer', 'value': 'Female'},
                    {'label': 'Hombre', 'value': 'Male'},
                    {'label': 'Otro', 'value': 'Other'}
                ],
                value='Female',
                id='gender'
            )
        ]),
        # Hipertensión
        html.Div([
            html.Label("Hipertensión"),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': 1},
                    {'label': 'No', 'value': 0}
                ],
                value=0,
                id='hypertension'
            )
        ]),
        # Enfermedad cardíaca
        html.Div([
            html.Label("Enfermedad cardíaca"),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': 1},
                    {'label': 'No', 'value': 0}
                ],
                value=0,
                id='heart_disease'
            )
        ]),
        # Casado
        html.Div([
            html.Label("¿Alguna vez casado?"),
            dcc.RadioItems(
                options=[
                    {'label': 'Sí', 'value': 1},
                    {'label': 'No', 'value': 0}
                ],
                value=0,
                id='ever_married'
            )
        ])
    ], style={'display': 'flex', 'justify-content': 'space-between'}),

    # Fila 2
    html.Div([
        # Residencia
        html.Div([
            html.Label("Tipo de residencia"),
            dcc.RadioItems(
                options=[
                    {'label': 'Rural', 'value': 'Rural'},
                    {'label': 'Urbana', 'value': 'Urban'}
                ],
                value='Urban',
                id='residence_type'
            )
        ]),
        # Tipo de fumador
        html.Div([
            html.Label("Tipo de fumador"),
            dcc.RadioItems(
                options=[
                    {'label': 'Fumador', 'value': 'smokes'},
                    {'label': 'Fumador regular', 'value': 'formerly smoked'},
                    {'label': 'No fumador', 'value': 'never smoked'}
                ],
                value='never smoked',
                id='smoking_status'
            )
        ]),
        # Edad
        html.Div([
            html.Label("Edad"),
            dcc.Input(id="age", type="number", value=30)
        ]),
        # BMI
        html.Div([
            html.Label("Índice de masa corporal"),
            dcc.Input(id="bmi", type="number", value=25)
        ])
    ], style={'display': 'flex', 'justify-content': 'space-between'}),

    # Fila 3
    html.Div([
        # Glucosa
        html.Div([
            html.Label("Promedio de glucosa en sangre"),
            dcc.Input(id="avg_glucose_level", type="number", value=100)
        ]),
        # Tipo de trabajo
        html.Div([
            html.Label("Tipo de trabajo"),
            dcc.Dropdown(
                id='work_type',
                options=[
                    {'label': 'Empleado privado', 'value': 'Private'},
                    {'label': 'Gobierno', 'value': 'Govt_job'},
                    {'label': 'Trabajo independiente', 'value': 'Self-employed'},
                    {'label': 'Desempleado', 'value': 'children'},
                    {'label': 'Nunca trabajó', 'value': 'Never_worked'}
                ],
                value='Private'
            )
        ])
    ], style={'display': 'flex', 'justify-content': 'space-between'}),

    # Botón de envío
    html.Button("Predecir", id="predict-button", n_clicks=0),

    # Resultado
    html.H2("Predicción de riesgo de ACV"),
    dcc.Graph(id='gauge', config={'displayModeBar': False})
])

# ------------------------------------------------------------------------------------------------------
#---------------------------------- Callback para actualizar la predicción -----------------------------
# ------------------------------------------------------------------------------------------------------
@app.callback(
    Output('gauge', 'figure'),
    [Input('predict-button', 'n_clicks')],
    [State('gender', 'value'), State('hypertension', 'value'), State('heart_disease', 'value'),
     State('ever_married', 'value'), State('residence_type', 'value'), State('smoking_status', 'value'),
     State('age', 'value'), State('bmi', 'value'), State('avg_glucose_level', 'value'), State('work_type', 'value')]
)
def update_gauge(n_clicks, gender, hypertension, heart_disease, ever_married, residence_type, smoking_status, age, bmi, avg_glucose_level, work_type):
    if n_clicks == 0:
        # Si no se ha presionado el botón, no se actualiza el gráfico
        return go.Figure(go.Indicator(
            mode="gauge+number",
            value= 0,
            title={'text': "Probabilidad de ACV (%)"},
            gauge={'axis': {'range': [0, 100]}}
        ))

    # Preparar datos para la API
    payload = {
        "gender": gender,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "ever_married": ever_married,
        "Residence_type": residence_type,
        "smoking_status": smoking_status,
        "age": age,
        "bmi": bmi,
        "avg_glucose_level": avg_glucose_level,
        "work_type": work_type
    }

    # Hacer POST a la API
    try:
        response = requests.post(API_URL, json=payload)
        prediction = response.json().get("prediction", 0) * 100
    except Exception as e:
        prediction = 0  # Si ocurre un error, predicción es 0

    # Crear el gráfico de gauge
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction,
        title={'text': "Probabilidad de ACV (%)", 'font': {'color': '#B71C1C'}},
        gauge={'axis': {'range': [0, 100], 'tickwidth': 2},
               'steps': [{'range': [0, 33], 'color': "#81C784"},
                         {'range': [33, 66], 'color': "#FFEB3B"},
                         {'range': [66, 100], 'color': "#E57373"}]},
    ))
    return fig


# ------------------------------------------------------------------------------------------------------
#-------------------------------------------- Correr APP -----------------------------------------------
# ------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
