import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Modell laden
model = joblib.load("models/random_forest.pkl")

# Daten laden
df = pd.read_csv("data/raw/wine_quality_combined.csv")

# Wein-Typ umwandeln
df["wine_type"] = df["wine_type"].map({
    "red": 0,
    "white": 1
})

# Features
X = df.drop("quality", axis=1)

# Feature Importance berechnen
importances = model.feature_importances_

feature_importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importances
})

feature_importance_df = feature_importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\n===== FEATURE IMPORTANCE =====")
print(feature_importance_df)

# Ordner erstellen
import os
os.makedirs("data/processed", exist_ok=True)

# CSV speichern
feature_importance_df.to_csv(
    "data/processed/feature_importance.csv",
    index=False
)

# Diagramm erstellen
plt.figure(figsize=(10, 6))

plt.barh(
    feature_importance_df["Feature"],
    feature_importance_df["Importance"]
)

plt.gca().invert_yaxis()

plt.title("Random Forest Feature Importance")
plt.xlabel("Importance")
plt.tight_layout()

plt.savefig(
    "data/processed/feature_importance.png"
)

plt.show()

print("\nFeature Importance gespeichert:")
print("data/processed/feature_importance.csv")
print("data/processed/feature_importance.png")