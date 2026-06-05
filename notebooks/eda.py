import pandas as pd

# Daten laden
df = pd.read_csv("data/raw/wine_quality_combined.csv")

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== FEHLENDE WERTE =====")
print(df.isnull().sum())

print("\n===== STATISTIKEN =====")
print(df.describe())

print("\n===== QUALITÄTSVERTEILUNG =====")
print(df["quality"].value_counts().sort_index())

print("\n===== WEINTYPEN =====")
print(df["wine_type"].value_counts())