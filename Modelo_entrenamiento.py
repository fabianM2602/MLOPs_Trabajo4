
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Cargar dataset
df = pd.read_csv("C:/Users/fabia/Documents/MLOPS/MLOPs_Trabajo4/breast_cancer_data.csv")

# Separar características y etiqueta
print(df.columns)
print(df.head())
X = df.drop(["id", "Unnamed: 32", "diagnosis"], axis=1)
y = df["diagnosis"]

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluar modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Guardar modelo
joblib.dump(model, "model.joblib")
print("Modelo guardado como model.joblib")
