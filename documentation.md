# AI Applications Project Documentation

## Project Metadata

* Project title: AI Wine Advisor
* Student: Arianit Salihi
* GitHub repository URL: https://github.com/Arianit1818/wine-ai-advisor
* Deployment URL: https://huggingface.co/spaces/Salihari/wine-ai-advisor
* Submission date: 07.06.2026

### Mandatory Setup Checks

* [x] At least 2 blocks selected
* [x] Multiple and different data sources used
* [x] Deployment URL provided
* [x] Required GitHub users added to repository (`jasminh`, `bkuehnis`)

## Selected AI Blocks

* [x] ML Numeric Data
* [x] NLP
* [ ] Computer Vision

Primary blocks used for core solution (choose 2):

* Primary block 1: ML Numeric Data
* Primary block 2: NLP

---

# 1. Project Foundation (Short)

## 1.1 Problem Definition

* Problem statement:

Wine quality assessment usually requires expert knowledge and sensory evaluation. Most users cannot estimate wine quality based solely on physicochemical measurements.

* Goal:

Develop an AI application that predicts wine quality using machine learning and provides understandable natural language explanations of the prediction.

* Success criteria:

  * Accurate wine quality prediction
  * Comparison of multiple machine learning models
  * Human-readable NLP explanations
  * Functional web application deployment
  * Clear integration between ML and NLP

## 1.2 Integration Logic

* How the selected blocks interact:

The ML component predicts wine quality based on physicochemical wine features. The NLP component receives the prediction and relevant feature information and generates an explanation for the user.

* Data and output flow between blocks:

Wine Features
→ Random Forest Prediction
→ Quality Score
→ NLP Explanation
→ User Interface

---

# 2. Block Documentation

## 2A. ML Numeric Data

### 2A.1 Data Source(s)

| Entry | Source name or link                   | Type | Size       | Role in this block      |
| ----- | ------------------------------------- | ---- | ---------- | ----------------------- |
| 1     | UCI Wine Quality Dataset (Red Wine)   | CSV  | 1,599 rows | Training and evaluation |
| 2     | UCI Wine Quality Dataset (White Wine) | CSV  | 4,898 rows | Training and evaluation |
| 3     | Combined Wine Dataset                 | CSV  | 6,497 rows | Final ML dataset        |

### 2A.2 Preprocessing and Features

* Cleaning steps:

  * Checked for missing values
  * Verified data types
  * Combined red and white wine datasets

* Preprocessing steps:

  * Encoded wine type as a numerical feature
  * Split dataset into training and testing data
  * Separated target variable from predictors

* Feature engineering and selection:

  * Added wine_type feature
  * Used all physicochemical measurements as input features
  * Generated feature importance scores using Random Forest

### 2A.3 Model Selection

* Models tested:

  * Linear Regression
  * Random Forest Regressor
  * Gradient Boosting Regressor

* Why these models were chosen:

Linear Regression was selected as a baseline model. Random Forest and Gradient Boosting were selected because they can model non-linear relationships and feature interactions.

### 2A.4 Model Comparison and Iterations

| Iteration | Objective                     | Key changes            | Models used       | Main metric | Change vs previous                   |
| --------- | ----------------------------- | ---------------------- | ----------------- | ----------- | ------------------------------------ |
| 1         | Establish baseline            | Basic regression model | Linear Regression | R² = 0.267  | Baseline                             |
| 2         | Improve prediction quality    | Ensemble learning      | Random Forest     | R² = 0.499  | Significant improvement              |
| 3         | Evaluate alternative ensemble | Boosting approach      | Gradient Boosting | R² = 0.376  | Lower performance than Random Forest |

### 2A.5 Evaluation and Error Analysis

* Metrics used:

  * Mean Absolute Error (MAE)
  * Root Mean Squared Error (RMSE)
  * R² Score

* Final results:

Linear Regression

* MAE = 0.564
* RMSE = 0.736
* R² = 0.267

Random Forest

* MAE = 0.437
* RMSE = 0.608
* R² = 0.499

Gradient Boosting

* MAE = 0.532

* RMSE = 0.679

* R² = 0.376

* Error patterns and likely causes:

Wine quality ratings are partly subjective and influenced by factors that are not present in the dataset. In addition, extreme quality classes occur only rarely, which limits model performance for those cases.

### 2A.6 Integration with Other Block(s)

* Inputs received from other block(s):
  None.

* Outputs provided to other block(s):

The predicted wine quality score is passed to the NLP module for explanation generation.

---

## 2B. NLP

### 2B.1 Data Source(s)

| Entry | Source name or link          | Type                    | Size        | Role in this block               |
| ----- | ---------------------------- | ----------------------- | ----------- | -------------------------------- |
| 1     | Predicted wine quality score | Numeric output          | 1 value     | Input for explanation generation |
| 2     | Wine feature values          | Structured data         | 12 features | Context for explanation          |
| 3     | Prompt templates             | Internal text templates | N/A         | Explanation generation           |

### 2B.2 Preprocessing and Prompt Design

* Text preprocessing:

No text cleaning was required because the explanations are generated from structured model outputs.

* Prompt design or retrieval setup:

Two explanation approaches were implemented:

* Prompt A: Basic explanation
* Prompt B: Detailed explanation including interpretation of important wine characteristics

### 2B.3 Approach Selection

* Approach used:

Prompt engineering and rule-based NLP generation.

* Alternatives considered:

  * Static output text
  * LLM-based explanations

Prompt engineering was selected because it provides reproducible and deterministic explanations without requiring external API services.

### 2B.4 Comparison and Iterations

| Iteration | Objective                  | Key changes                  | Model or prompt setup | Main metric or qualitative check | Change vs previous |
| --------- | -------------------------- | ---------------------------- | --------------------- | -------------------------------- | ------------------ |
| 1         | Generate basic explanation | Generic template             | Prompt A              | Readability                      | Baseline           |
| 2         | Improve usefulness         | Feature-specific explanation | Prompt B              | Informativeness                  | Improved           |
| 3         | Full integration           | Combined ML-NLP workflow     | Final version         | User experience                  | Better interaction |

### 2B.5 Evaluation and Error Analysis

* Evaluation strategy:

Qualitative comparison of generated explanations.

* Results:

Prompt B provided more informative explanations by referencing specific wine properties and explaining why they may influence wine quality.

* Error patterns and likely causes:

The explanations are rule-based and cannot fully represent all relationships learned by the machine learning model. Complex interactions between variables may be simplified.

### 2B.6 Integration with Other Block(s)

* Inputs received from other block(s):

Predicted wine quality score generated by the Random Forest model.

* Outputs provided to other block(s):

Human-readable explanation displayed within the Streamlit application.

---

## 2C. Computer Vision

N/A

---

# 3. Deployment

* Deployment URL:

https://huggingface.co/spaces/Salihari/wine-ai-advisor

* Main user flow:

1. User enters wine characteristics.
2. The Random Forest model predicts wine quality.
3. Feature importance information is displayed.
4. NLP explanations are generated.
5. Results are shown in the Streamlit interface.

* Screenshot or short demo:

Included screenshots:

* Main application interface
* Prediction result
* Feature importance visualization
* NLP explanation comparison

---

# 4. Execution Instructions

* Environment setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

* Data setup:

```bash
python download_data.py
```

* Training command(s):

```bash
python src/train_model.py
python src/feature_importance.py
python notebooks/eda_visuals.py
```

* Inference/run command(s):

```bash
streamlit run app.py
```

* Reproducibility notes:

All experiments were executed using the same dataset and reproducible preprocessing pipeline. The trained Random Forest model is stored and reused for inference.

---

# 5. Optional Bonus Evidence

* [ ] Third selected block implemented with strong quality
* [ ] More than two data sources used with clear added value
* [x] A core section is done exceptionally well
* [x] Extended evaluation
* [ ] Ethics, bias, or fairness analysis
* [ ] Creative or exceptional use case

Evidence for selected bonus items:

* Comparison of three machine learning models
* Multiple evaluation metrics
* Feature importance analysis
* Exploratory Data Analysis (EDA)
* Multiple NLP explanation strategies
* Integrated ML and NLP workflow
* Interactive Streamlit deployment
* Online deployment via Hugging Face Spaces
* GitHub repository with reproducible implementation

