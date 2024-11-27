from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Ruta del modelo entrenado
MODEL_PATH = "/home/ubuntu/env/lib/python3.12/site-packages/model/trained/model.pkl"

# Cargar el pipeline completo
try:
    loaded_model = joblib.load(MODEL_PATH)
    scaler = loaded_model["scaler"]
    pca = loaded_model["pca"]
    model = loaded_model["model"]
    feature_columns = loaded_model["feature_columns"]
except Exception as e:
    raise RuntimeError(f"Error al cargar el modelo: {e}")

# Crear la aplicación FastAPI
app = FastAPI()

# Modelo de datos de entrada
class InputData(BaseModel):
    gender: str
    hypertension: int
    heart_disease: int
    ever_married: int
    Residence_type: str
    smoking_status: str
    age: float
    bmi: float
    avg_glucose_level: float
    work_type: str

# Endpoint de predicción
@app.post("/predict")
async def predict(data: InputData):
    try:
        # Convertir los datos de entrada en un DataFrame
        input_dict = data.dict()
        input_df = pd.DataFrame([input_dict])

        # One-hot encoding para las variables categóricas
        input_encoded = pd.get_dummies(input_df)
        input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)

        # Aplicar scaler
        input_scaled = scaler.transform(input_encoded)

        # Aplicar PCA
        input_pca = pca.transform(input_scaled)

        # Realizar predicción (probabilidad de la clase positiva)
        probabilities = model.predict_proba(input_pca)
        probability_of_positive_class = probabilities[0][1]

        return {"prediction": float(probability_of_positive_class)}

    except Exception as e:
        return {"error": str(e)}
