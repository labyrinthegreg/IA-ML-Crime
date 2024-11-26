from fastapi import FastAPI, HTTPException
from app.pipeline import data_pipeline

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

CSV_PATH = "./data/train.csv"

@app.post("/predict/")
async def predict(input_data: dict):
    try:
        result = data_pipeline(CSV_PATH, input_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))