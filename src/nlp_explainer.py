def explain_prediction(input_data, predicted_quality):
    alcohol = input_data["alcohol"]
    volatile_acidity = input_data["volatile acidity"]
    residual_sugar = input_data["residual sugar"]
    pH = input_data["pH"]
    sulphates = input_data["sulphates"]
    wine_type = "white wine" if input_data["wine_type"] == 1 else "red wine"

    explanation_parts = []

    if predicted_quality >= 7:
        quality_text = "high"
    elif predicted_quality >= 5:
        quality_text = "medium"
    else:
        quality_text = "low"

    explanation_parts.append(
        f"The model predicts a {quality_text} quality score of {predicted_quality} out of 10 for this {wine_type}."
    )

    if alcohol >= 11:
        explanation_parts.append(
            "The alcohol level is relatively high, which is often associated with better perceived wine quality."
        )
    elif alcohol < 9.5:
        explanation_parts.append(
            "The alcohol level is rather low, which may reduce the predicted quality score."
        )

    if volatile_acidity > 0.6:
        explanation_parts.append(
            "The volatile acidity is high, which can negatively affect aroma and taste."
        )
    elif volatile_acidity < 0.3:
        explanation_parts.append(
            "The volatile acidity is low, which is generally positive for wine quality."
        )

    if residual_sugar > 12:
        explanation_parts.append(
            "The wine has a high residual sugar level, which may indicate a sweeter wine style."
        )

    if pH < 3.1:
        explanation_parts.append(
            "The pH value is relatively low, meaning the wine is more acidic."
        )
    elif pH > 3.6:
        explanation_parts.append(
            "The pH value is relatively high, meaning the wine is less acidic."
        )

    if sulphates > 0.7:
        explanation_parts.append(
            "The sulphate level is relatively high, which may support wine stability and freshness."
        )

    explanation_parts.append(
        "This explanation is based on selected input features and should be interpreted as supportive information, not as a professional wine tasting result."
    )

    return " ".join(explanation_parts)


def compare_prompt_styles(input_data, predicted_quality):
    basic_explanation = (
        f"This wine receives a predicted quality score of {predicted_quality}. "
        f"The prediction is mainly influenced by values such as alcohol, acidity, sugar, pH and sulphates."
    )

    detailed_explanation = explain_prediction(input_data, predicted_quality)

    return {
        "Prompt A - Basic explanation": basic_explanation,
        "Prompt B - Detailed explanation": detailed_explanation
    }


if __name__ == "__main__":
    sample_wine = {
        "fixed acidity": 7.4,
        "volatile acidity": 0.70,
        "citric acid": 0.00,
        "residual sugar": 1.9,
        "chlorides": 0.076,
        "free sulfur dioxide": 11.0,
        "total sulfur dioxide": 34.0,
        "density": 0.9978,
        "pH": 3.51,
        "sulphates": 0.56,
        "alcohol": 9.4,
        "wine_type": 0
    }

    predicted_quality = 5.01

    explanations = compare_prompt_styles(sample_wine, predicted_quality)

    for title, explanation in explanations.items():
        print("\n" + title)
        print(explanation)