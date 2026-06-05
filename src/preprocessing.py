import pandas as pd
from sklearn.model_selection import train_test_split

# Daten laden
df = pd.read_csv("data/raw/wine_quality_combined.csv")

# Wein-Typ in Zahlen umwandeln
df["wine_type"] = df["wine_type"].map({
    "red": 0,
    "white": 1
})

# Features und Zielvariable
X = df.drop("quality", axis=1)
y = df["quality"]

# Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Trainingsdaten:", X_train.shape)
print("Testdaten:", X_test.shape)