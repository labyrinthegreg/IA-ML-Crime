from fastapi import FastAPI
import pandas as pd
import pickle

app = FastAPI()

with open('pipeline_model.pkl', 'rb') as file:
    model = pickle.load(file)
print("Pipeline chargée avec succès.")

@app.post("/predict/")
def predict(input_data: dict):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)

    return {"prediction": prediction[0]}
