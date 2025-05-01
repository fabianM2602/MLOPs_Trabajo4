from fastapi import FastAPI
from pydantic import BaseModel
import multiprocessing
multiprocessing.set_start_method("spawn", force=True)

import joblib
import numpy as np

# Cargar el modelo entrenado
model = joblib.load("model.joblib")

# Inicializar la API
app = FastAPI(title="Breast Cancer Predictor API")

# Definir los datos de entrada con Pydantic
class CancerInput(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float
    radius_se: float
    texture_se: float
    perimeter_se: float
    area_se: float
    smoothness_se: float
    compactness_se: float
    concavity_se: float
    concave_points_se: float
    symmetry_se: float
    fractal_dimension_se: float
    radius_worst: float
    texture_worst: float
    perimeter_worst: float
    area_worst: float
    smoothness_worst: float
    compactness_worst: float
    concavity_worst: float
    concave_points_worst: float
    symmetry_worst: float
    fractal_dimension_worst: float

# Endpoint de predicción
@app.post("/predict")
def predict(data: CancerInput):
    input_array = np.array([list(data.dict().values())])
    prediction = model.predict(input_array)
    result = "Maligno" if prediction[0] == 1 else "Benigno"
    return {"predicción": result}


