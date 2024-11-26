import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def load_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path).sample(frac=0.1)
    df['Dates'] = pd.to_datetime(df['Dates']).dt.to_period('M')
    return df

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df_train = df[['Dates', 'Category', 'X', 'Y']].copy()
    enc = LabelEncoder()
    df_train['Dates'] = enc.fit_transform(df_train['Dates'])
    df_train['Category'] = enc.fit_transform(df_train['Category'])
    return df_train, enc

def train_model(df: pd.DataFrame):
    x_train, x_test, y_train, y_test = train_test_split(df[['Dates', 'X', 'Y']], df['Category'], test_size=0.2)
    model = LogisticRegression()
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    return model, score

def make_prediction(model, enc, input_data: dict) -> dict:
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    decoded = enc.inverse_transform(prediction)
    return {"prediction": decoded[0]}

def data_pipeline(csv_path: str, input_data: dict):
    df = load_csv(csv_path)
    df_train, enc = preprocess_data(df)
    model, score = train_model(df_train)
    prediction = make_prediction(model, enc, input_data)
    return {"model_score": score, "prediction": prediction}
