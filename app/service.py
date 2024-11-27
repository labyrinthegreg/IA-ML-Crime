import pandas as pd

def make_prediction(pipeline, input_data: dict) -> dict:
    input_df = pd.DataFrame([input_data])

    prediction = pipeline.predict(input_df)
    return {"prediction": prediction[0]}