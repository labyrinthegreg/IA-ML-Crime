import pickle
from fastapi import FastAPI
from app.service import make_prediction

app = FastAPI()

try:
    with open('../pipeline_model.pkl', 'rb') as file:
        model = pickle.load(file)
    print("Pipeline chargée avec succès.")
except FileNotFoundError:
    print(f"Erreur : le fichier 'pipeline_model.pkl' est introuvable.")
    model = None
except Exception as e:
    print(f"Erreur lors du chargement de la pipeline : {e}")
    model = None

@app.get("/")
def read_root():
    return {"message": "API active"}

@app.post("/predict/")
def predict(input_data: dict):
    return make_prediction(model, input_data)
