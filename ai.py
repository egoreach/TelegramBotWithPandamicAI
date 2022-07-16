import pandas as pd

from catboost import CatBoostRegressor


df = pd.read_csv("clean.csv")
text_features = ['name', 'district', 'subject', 'region_x']  # useful variable

model = CatBoostRegressor()
model.load_model(fname="model.cbm")


def get_city_prediction(city_name: str) -> (float, float, float):
    row = df.loc[df['name'] == city_name]
    prediction = round(model.predict(row.drop(text_features + ['inf_rate'],
                                              axis=1))[0], 10)
    real = round(float(row.inf_rate), 10)
    return prediction, real, abs(prediction - real)
