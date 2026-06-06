import pandas as pd
import streamlit as st
from PIL import Image

from src.predict import predict_quality
from src.nlp_explainer import compare_prompt_styles
from src.cv_analyzer import analyze_wine_image, generate_image_explanation


st.set_page_config(
    page_title="AI Wine Advisor",
    page_icon="🍷",
    layout="wide"
)


def get_quality_category(prediction):
    if prediction >= 7:
        return "High quality", "🟢"
    elif prediction >= 5:
        return "Medium quality", "🟡"
    else:
        return "Low quality", "🔴"


def load_feature_importance():
    return pd.read_csv("data/processed/feature_importance.csv")


st.title("🍷 AI Wine Advisor")

st.write(
    "This app predicts wine quality based on physicochemical properties, "
    "explains the prediction using NLP, and optionally analyzes an uploaded wine image."
)

st.sidebar.header("Wine Input Features")

wine_type_label = st.sidebar.selectbox(
    "Wine Type",
    ["Red wine", "White wine"]
)

wine_type = 0 if wine_type_label == "Red wine" else 1

fixed_acidity = st.sidebar.slider(
    "Fixed acidity",
    min_value=3.0,
    max_value=16.0,
    value=7.4,
    step=0.1
)

volatile_acidity = st.sidebar.slider(
    "Volatile acidity",
    min_value=0.05,
    max_value=1.60,
    value=0.70,
    step=0.01
)

citric_acid = st.sidebar.slider(
    "Citric acid",
    min_value=0.0,
    max_value=1.70,
    value=0.00,
    step=0.01
)

residual_sugar = st.sidebar.slider(
    "Residual sugar",
    min_value=0.5,
    max_value=70.0,
    value=1.9,
    step=0.1
)

chlorides = st.sidebar.slider(
    "Chlorides",
    min_value=0.005,
    max_value=0.650,
    value=0.076,
    step=0.001
)

free_sulfur_dioxide = st.sidebar.slider(
    "Free sulfur dioxide",
    min_value=1.0,
    max_value=300.0,
    value=11.0,
    step=1.0
)

total_sulfur_dioxide = st.sidebar.slider(
    "Total sulfur dioxide",
    min_value=5.0,
    max_value=450.0,
    value=34.0,
    step=1.0
)

density = st.sidebar.slider(
    "Density",
    min_value=0.9800,
    max_value=1.0400,
    value=0.9978,
    step=0.0001,
    format="%.4f"
)

pH = st.sidebar.slider(
    "pH",
    min_value=2.70,
    max_value=4.10,
    value=3.51,
    step=0.01
)

sulphates = st.sidebar.slider(
    "Sulphates",
    min_value=0.20,
    max_value=2.00,
    value=0.56,
    step=0.01
)

alcohol = st.sidebar.slider(
    "Alcohol",
    min_value=8.0,
    max_value=15.0,
    value=9.4,
    step=0.1
)

input_data = {
    "fixed acidity": fixed_acidity,
    "volatile acidity": volatile_acidity,
    "citric acid": citric_acid,
    "residual sugar": residual_sugar,
    "chlorides": chlorides,
    "free sulfur dioxide": free_sulfur_dioxide,
    "total sulfur dioxide": total_sulfur_dioxide,
    "density": density,
    "pH": pH,
    "sulphates": sulphates,
    "alcohol": alcohol,
    "wine_type": wine_type
}

left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader("Selected Wine Properties")
    input_df = pd.DataFrame([input_data]).T
    input_df.columns = ["Value"]
    st.dataframe(input_df, width="stretch")

with right_col:
    st.subheader("Model Information")
    st.write("The prediction is generated with a Random Forest Regressor.")
    st.write("The model was selected after comparing three models:")
    st.write("- Linear Regression")
    st.write("- Random Forest")
    st.write("- Gradient Boosting")

st.divider()

st.subheader("Optional Computer Vision Input")

uploaded_image = st.file_uploader(
    "Upload a wine bottle or wine label image",
    type=["jpg", "jpeg", "png"]
)

image_analysis = None
image_explanation = None

if uploaded_image is not None:
    image = Image.open(uploaded_image)

    img_col1, img_col2 = st.columns([1, 1])

    with img_col1:
        st.image(image, caption="Uploaded Wine Image", width=350)

    with img_col2:
        image_analysis = analyze_wine_image(image)
        image_explanation = generate_image_explanation(image_analysis)

        st.markdown("### Computer Vision Analysis")
        st.dataframe(
            pd.DataFrame([image_analysis]).T.rename(columns={0: "Value"}),
            width="stretch"
        )

        st.markdown("### Visual Explanation")
        st.write(image_explanation)

if st.button("Predict Wine Quality"):
    prediction = predict_quality(input_data)
    category, emoji = get_quality_category(prediction)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Predicted Wine Quality")
        st.metric(
            label="Quality Score",
            value=f"{prediction} / 10"
        )

    with col2:
        st.subheader("Quality Category")
        st.metric(
            label="Category",
            value=f"{emoji} {category}"
        )

    st.divider()

    st.subheader("Top Influencing Features")

    feature_importance_df = load_feature_importance()
    top_features = feature_importance_df.head(5)

    st.dataframe(top_features, width="stretch")

    st.bar_chart(
        top_features.set_index("Feature")["Importance"]
    )

    st.divider()

    explanations = compare_prompt_styles(input_data, prediction)

    st.subheader("NLP Explanation Comparison")

    st.markdown("### Prompt A - Basic Explanation")
    st.write(explanations["Prompt A - Basic explanation"])

    st.markdown("### Prompt B - Detailed Explanation")
    st.write(explanations["Prompt B - Detailed explanation"])

    if image_explanation is not None:
        st.markdown("### Additional Computer Vision Explanation")
        st.write(image_explanation)

    st.info(
        "The ML prediction is directly used as input for the NLP explanation. "
        "If an image is uploaded, the Computer Vision component adds visual information "
        "to the overall analysis."
    )