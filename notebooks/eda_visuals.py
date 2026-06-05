import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ordner für Grafiken erstellen
os.makedirs("data/processed", exist_ok=True)

# Daten laden
df = pd.read_csv("data/raw/wine_quality_combined.csv")

# ----------------------------------
# 1. Qualitätsverteilung
# ----------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    x="quality",
    data=df
)

plt.title("Wine Quality Distribution")
plt.xlabel("Quality Score")
plt.ylabel("Number of Wines")

plt.tight_layout()

plt.savefig(
    "data/processed/quality_distribution.png"
)

plt.close()

# ----------------------------------
# 2. Wein-Typ-Verteilung
# ----------------------------------

plt.figure(figsize=(6, 5))

sns.countplot(
    x="wine_type",
    data=df
)

plt.title("Wine Type Distribution")
plt.xlabel("Wine Type")
plt.ylabel("Number of Wines")

plt.tight_layout()

plt.savefig(
    "data/processed/wine_type_distribution.png"
)

plt.close()

# ----------------------------------
# 3. Korrelationsmatrix
# ----------------------------------

correlation_df = df.copy()

correlation_df["wine_type"] = correlation_df["wine_type"].map({
    "red": 0,
    "white": 1
})

plt.figure(figsize=(12, 8))

sns.heatmap(
    correlation_df.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Feature Correlation Matrix")

plt.tight_layout()

plt.savefig(
    "data/processed/correlation_matrix.png"
)

plt.close()

print("\nEDA Visualizations created successfully:")
print("data/processed/quality_distribution.png")
print("data/processed/wine_type_distribution.png")
print("data/processed/correlation_matrix.png")