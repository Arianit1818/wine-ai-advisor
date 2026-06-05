---

title: AI Wine Advisor
emoji: 🍷
colorFrom: red
colorTo: purple
sdk: streamlit
sdk_version: "1.50.0"
python_version: "3.9"
app_file: app.py
pinned: false
-------------

# 🍷 AI Wine Advisor

AI Wine Advisor is an AI application that predicts wine quality using machine learning and explains the prediction using natural language processing (NLP).

This project was developed for the AI Applications course and combines the following AI blocks:

* ML Numeric Data
* NLP (Natural Language Processing)

---

# Live Demo

Hugging Face Deployment:

https://huggingface.co/spaces/Salihari/wine-ai-advisor

GitHub Repository:

https://github.com/Arianit1818/wine-ai-advisor

---

# Project Overview

Wine quality is difficult to estimate without expert knowledge. This application predicts wine quality based on physicochemical properties and provides an understandable explanation of the prediction.

Workflow:

Wine Features
→ Machine Learning Prediction
→ Quality Score
→ NLP Explanation
→ Streamlit User Interface

---

# Features

## Machine Learning

* Wine quality prediction
* Comparison of multiple models:

  * Linear Regression
  * Random Forest Regressor
  * Gradient Boosting Regressor
* Model evaluation using:

  * MAE
  * RMSE
  * R² Score
* Feature importance analysis

## NLP

* Automatic explanation generation
* Comparison of multiple explanation styles
* Human-readable prediction interpretation

## User Interface

* Interactive Streamlit dashboard
* Adjustable wine characteristics
* Quality category classification
* Feature importance visualization
* NLP explanations

---

# Dataset

Source:

UCI Machine Learning Repository – Wine Quality Dataset

Datasets used:

* Red Wine Quality Dataset
* White Wine Quality Dataset

Combined dataset:

* 6,497 wine samples

Features include:

* Fixed acidity
* Volatile acidity
* Citric acid
* Residual sugar
* Chlorides
* Free sulfur dioxide
* Total sulfur dioxide
* Density
* pH
* Sulphates
* Alcohol
* Wine type

Target variable:

* Wine Quality (3–9)

---

# Model Performance

## Linear Regression

* MAE = 0.564
* RMSE = 0.736
* R² = 0.267

## Random Forest (Selected Model)

* MAE = 0.437
* RMSE = 0.608
* R² = 0.499

## Gradient Boosting

* MAE = 0.532
* RMSE = 0.679
* R² = 0.376

The Random Forest model achieved the best performance and was selected for deployment.

---

# Project Structure

```text
wine-ai-advisor/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│
├── screenshots/
│
├── src/
│
├── app.py
├── README.md
├── documentation.md
├── requirements.txt
└── .gitignore
```

---

# Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Data Preparation

```bash
python download_data.py
```

---

# Training

```bash
python src/train_model.py
```

Generate feature importance:

```bash
python src/feature_importance.py
```

Generate visualizations:

```bash
python notebooks/eda_visuals.py
```

---

# Run Application

```bash
streamlit run app.py
```

---

# Screenshots

See:

* screenshots/main_interface.png
* screenshots/prediction_result.png
* screenshots/feature_importance_nlp.png

---

# Author

Arianit Salihi

AI Applications Project – 2026
