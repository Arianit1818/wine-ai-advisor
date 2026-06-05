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
  Wine quality assessment usually requires expert knowledge and sensory evaluation. Most users cannot estimate wine quality based on physicochemical measurements alone.

* Goal:
  Develop an AI application that predicts wine quality from measurable wine characteristics and provides a human-readable explanation of the prediction.

* Success criteria:

  * Accurate wine quality prediction
  * Comparison of multiple machine learning models
  * Natural language explanation of predictions
  * Functional web application deployment

## 1.2 Integration Logic

* How the selected blocks interact:
  The machine learning model predicts wine quality based on numerical wine characteristics. The NLP component receives the prediction and generates a user-friendly explanation.

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

  * Encoded wine type into numerical values
  * Split dataset into training and testing sets
  * Separated target variable from features

* Feature engineering and selection:

  * Added wine_type as an additional feature
  * Used all physicochemical measurements as model inputs

### 2A.3 Model Selection

* Models tested:

  * Linear Regression
  * Random Forest Regressor
  * Gradient Boosting Regressor

* Why these models were chosen:
  Linear Regression was selected as a simple baseline model. Random Forest and Gradient Boosting were selected because they can capture non-linear relationships and complex feature interactions.

### 2A.4 Model Comparison and Iterations

| Iteration | Objective                       | Key changes            | Models used       | Main metric | Change vs previous                   |
| --------- | ------------------------------- | ---------------------- | ----------------- | ----------- | ------------------------------------ |
| 1         | Establish baseline              | Basic regression model | Linear Regression | R² = 0.267  | Baseline                             |
| 2         | Improve prediction performance  | Ensemble learning      | Random Forest     | R² = 0.499  | Significant improvement              |
| 3         | Test alternative ensemble model | Boosting approach      | Gradient Boosting | R² = 0.376  | Lower performance than Random Forest |

### 2A.5 Evaluation and Error Analysis

* Metrics used:

  * Mean Absolute Error (MAE)
  * Root Mean Squared Error (RMSE)
  * R² Score

* Final results:

Linear Regression:

* MAE = 0.564
* RMSE = 0.736
* R² = 0.267

Random Forest:

* MAE = 0.437
* RMSE = 0.608
* R² = 0.499

Gradient Boosting:

* MAE = 0.532

* RMSE = 0.679

* R² = 0.376

* Error patterns and likely causes:
  Wine quality is partially subjective and influenced by factors not included in the dataset. This limits the maximum achievable prediction accuracy. Extreme quality classes (3 and 9) are underrepresented, which may reduce prediction performance for these cases.

### 2A.6 Integration with Other Block(s)

* Inputs received from other block(s):
  None.

* Outputs provided to other block(s):
  The predicted wine quality score is passed to the NLP component for explanation generation.

---

## 2B. NLP

### 2B.1 Data Source(s)

| Entry | Source name or link          | Type            | Size        | Role in this block      |
| ----- | ---------------------------- | --------------- | ----------- | ----------------------- |
| 1     | Predicted wine quality score | Numeric output  | 1 value     | Input for explanation   |
| 2     | Wine feature values          | Structured data | 12 features | Context for explanation |
| 3     | Rule-based prompt templates  | Text templates  | Internal    | Explanation generation  |

### 2B.2 Preprocessing and Prompt Design

* Text preprocessing:
  No text cleaning was required because explanations were generated directly from structured model outputs.

* Prompt design or retrieval setup:
  Two explanation styles were implemented:

* Prompt A: Basic explanation

* Prompt B: Detailed explanation with interpretation of important wine characteristics

### 2B.3 Approach Selection

* Approach used:
  Prompt engineering and rule-based NLP generation.

* Alternatives considered:

  * Static text output
  * LLM-based explanations

Prompt engineering was selected because it provides deterministic and reproducible explanations without requiring external APIs.

### 2B.4 Comparison and Iterations

| Iteration | Objective                   | Key changes                  | Model or prompt setup | Main metric or qualitative check | Change vs previous  |
| --------- | --------------------------- | ---------------------------- | --------------------- | -------------------------------- | ------------------- |
| 1         | Generate simple explanation | Basic template               | Prompt A              | Understandability                | Baseline            |
| 2         | Improve interpretability    | Feature-specific explanation | Prompt B              | More informative output          | Improved usefulness |
| 3         | Integrated workflow         | Combined ML and NLP pipeline | Final version         | User experience                  | Better interaction  |

### 2B.5 Evaluation and Error Analysis

* Evaluation strategy:
  Qualitative comparison of generated explanations.

* Results:
  Prompt B produced more informative and useful explanations than Prompt A by referencing specific wine characteristics and quality factors.

* Error patterns and likely causes:
  The explanations are rule-based and cannot capture all complex interactions between features. Some explanations may oversimplify the underlying model behaviour.

### 2B.6 Integration with Other Block(s)

* Inputs received from other block(s):
  Predicted wine quality score from the Random Forest model.

* Outputs provided to other block(s):
  Human-readable explanation displayed in the Streamlit application.

---

## 2C. Computer Vision

N/A

---

# 3. Deployment

* Deployment URL:
  https://huggingface.co/spaces/Salihari/wine-ai-advisor

* Main user flow:

1. User enters wine characteristics.
2. Random Forest predicts wine quality.
3. Feature importance is displayed.
4. NLP generates explanations.
5. Results are shown in the Streamlit interface.

* Screenshot or short demo:

Screenshots of:

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
```

* Inference/run command(s):

```bash
streamlit run app.py
```

* Reproducibility notes:

All experiments use fixed random seeds where applicable. The Random Forest model is automatically saved and reused during prediction.

---

# 5. Optional Bonus Evidence

* [ ] Third selected block implemented with strong quality
* [ ] More than two data sources used with clear added value
* [x] A core section is done exceptionally well
* [x] Extended evaluation
* [ ] Ethics, bias, or fairness analysis
* [ ] Creative or exceptional use case

Evidence for selected bonus items:

The project includes:

* Comparison of three machine learning models
* Multiple evaluation metrics
* Feature importance analysis
* Exploratory data analysis
* Comparison of multiple NLP explanation strategies
* Integrated ML and NLP workflow
* Interactive web deployment

```
```
