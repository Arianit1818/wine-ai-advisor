import os
import pandas as pd

# Ordner erstellen falls nicht vorhanden
os.makedirs("data/raw", exist_ok=True)

# Datensätze laden
red_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
white_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"

red_wine = pd.read_csv(red_url, sep=";")
white_wine = pd.read_csv(white_url, sep=";")

# Wein-Typ hinzufügen
red_wine["wine_type"] = "red"
white_wine["wine_type"] = "white"

# Zusammenführen
wine_data = pd.concat([red_wine, white_wine], ignore_index=True)

# Speichern
wine_data.to_csv("data/raw/wine_quality_combined.csv", index=False)

print("\nDataset erfolgreich gespeichert!")
print(f"Anzahl Zeilen: {wine_data.shape[0]}")
print(f"Anzahl Spalten: {wine_data.shape[1]}")
print("\nErste 5 Zeilen:")
print(wine_data.head())