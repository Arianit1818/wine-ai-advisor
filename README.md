# 🍷 AI Wine Advisor

AI Wine Advisor is a machine learning and natural language processing application that predicts wine quality based on physicochemical wine characteristics and explains the prediction in natural language.

## Project Overview

The project combines two AI blocks:

* ML Numeric Data
* NLP (Natural Language Processing)

The machine learning component predicts wine quality using a trained Random Forest model. The NLP component generates human-readable explanations for the prediction.

### Workflow

Wine Features
→ Machine Learning Prediction
→ Quality Score
→ NLP Explanation
→ User Interface

---

## Features

### Machine Learning

* Wine quality prediction
* Comparison of three models:

  * Linear Regression
  * Random Forest Regressor
  * Gradient Boosting Regressor
* Model evaluation using:

  * MAE
  * RMSE
  * R² Score
* Feature importance analysis

### NLP

* Automatic explanation of predictions
* Comparison of two explanation styles:

  * Prompt A (Basic Explanation)
  * Prompt B (Detailed Explanation)

### Interactive Web Application

* User-friendly Streamlit interface
* Adjustable wine characteristics
* Quality category classification
* Feature importance visualization
* NLP explanation generation

---

## Dataset

The project uses the Wine Quality Dataset from the UCI Machine Learning Repository.

Datasets used:

* Red Wine Quality Dataset
* White Wine Quality Dataset

Combined dataset size:

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

Target:

* Wine quality (3–9)

---

## Model Performance

### Linear Regression

* MAE: 0.564
* RMSE: 0.736
* R²: 0.267

### Random Forest (Selected Model)

* MAE: 0.437
* RMSE: 0.608
* R²: 0.499

### Gradient Boosting

* MAE: 0.532
* RMSE: 0.679
* R²: 0.376

The Random Forest model achieved the best overall performance and was selected for deployment.

---

## Project Structure

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
├── src/
│
├── app.py
├── requirements.txt
├── README.md
├── documentation.md
└── Dockerfile
```

---

## Installation

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

## Data Preparation

Download and prepare the dataset:

```bash
python download_data.py
```

---

## Training

Train and compare machine learning models:

```bash
python src/train_model.py
```

Generate feature importance:

```bash
python src/feature_importance.py
```

Create EDA visualizations:

```bash
python notebooks/eda_visuals.py
```

---

## Run Application

Start the Streamlit application:

```bash
streamlit run app.py
```

---

## GitHub Repository

https://github.com/Arianit1818/wine-ai-advisor

## Deployment

Hugging Face Space:

https://huggingface.co/spaces/Salihari/wine-ai-advisor

---

## Author

Arianit Salihi

AI Applications Project 2026
