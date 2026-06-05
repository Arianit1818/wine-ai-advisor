import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Daten laden
df = pd.read_csv("data/raw/wine_quality_combined.csv")

# Wein-Typ in Zahlen umwandeln
df["wine_type"] = df["wine_type"].map({
    "red": 0,
    "white": 1
})

# Features und Zielvariable definieren
X = df.drop("quality", axis=1)
y = df["quality"]

# Trainings- und Testdaten erstellen
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ------------------
# Modell 1: Linear Regression
# ------------------

lr = LinearRegression()
lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

print("\n===== LINEAR REGRESSION =====")
print("MAE:", mean_absolute_error(y_test, lr_pred))
print("RMSE:", mean_squared_error(y_test, lr_pred) ** 0.5)
print("R²:", r2_score(y_test, lr_pred))

# ------------------
# Modell 2: Random Forest
# ------------------

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print("\n===== RANDOM FOREST =====")
print("MAE:", mean_absolute_error(y_test, rf_pred))
print("RMSE:", mean_squared_error(y_test, rf_pred) ** 0.5)
print("R²:", r2_score(y_test, rf_pred))

# ------------------
# Modell 3: Gradient Boosting
# ------------------

gb = GradientBoostingRegressor(
    random_state=42
)

gb.fit(X_train, y_train)

gb_pred = gb.predict(X_test)

print("\n===== GRADIENT BOOSTING =====")
print("MAE:", mean_absolute_error(y_test, gb_pred))
print("RMSE:", mean_squared_error(y_test, gb_pred) ** 0.5)
print("R²:", r2_score(y_test, gb_pred))

# Bestes Modell speichern
joblib.dump(rf, "models/random_forest.pkl")

print("\nRandom Forest gespeichert unter models/random_forest.pkl")