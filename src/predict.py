import joblib
import pandas as pd

MODEL_PATH = "models/random_forest.pkl"

FEATURE_COLUMNS = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol",
    "wine_type"
]


def load_model():
    model = joblib.load(MODEL_PATH)
    return model


def predict_quality(input_data):
    model = load_model()

    input_df = pd.DataFrame([input_data])
    input_df = input_df[FEATURE_COLUMNS]

    prediction = model.predict(input_df)[0]

    return round(float(prediction), 2)


if __name__ == "__main__":
    sample_wine = {
        "fixed acidity": 7.4,
        "volatile acidity": 0.70,
        "citric acid": 0.00,
        "residual sugar": 1.9,
        "chlorides": 0.076,
        "free sulfur dioxide": 11.0,
        "total sulfur dioxide": 34.0,
        "density": 0.9978,
        "pH": 3.51,
        "sulphates": 0.56,
        "alcohol": 9.4,
        "wine_type": 0
    }

    result = predict_quality(sample_wine)
    print(f"Predicted wine quality: {result}")