
import json
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

# Page setup
st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="centered"
)

# Find the project files
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "crop_yield_model.pkl"
OPTIONS_PATH = BASE_DIR / "models" / "app_options.json"


# Load the saved model
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


# Load dropdown options
@st.cache_data
def load_options():
    with open(OPTIONS_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


st.title("🌾 Crop Yield Prediction")
st.write(
    "Enter agricultural information to estimate crop yield "
    "using a machine learning model."
)

# Check whether the required files exist
if not MODEL_PATH.exists() or not OPTIONS_PATH.exists():
    st.error(
        "Required files are missing. Please check that "
        "crop_yield_model.pkl and app_options.json are inside "
        "the models folder."
    )
    st.stop()

try:
    model = load_model()
    options = load_options()
except Exception as error:
    st.error("Could not load the model or application options.")
    st.code(str(error))
    st.stop()


# Input form
st.header("Agricultural Details")

with st.form("prediction_form"):

    state = st.selectbox("State", options["State"])
    crop = st.selectbox("Crop", options["Crop"])
    season = st.selectbox("Season", options["Season"])

    year = st.number_input(
        "Year",
        min_value=int(options["Year_min"]),
        max_value=int(options["Year_max"]),
        value=int(options["Year_max"]),
        step=1
    )

    area = st.number_input(
        "Cultivated Area",
        min_value=0.000001,
        value=1.0
    )

    rainfall = st.number_input(
        "Annual Rainfall",
        min_value=0.0,
        value=1000.0
    )

    fertilizer = st.number_input(
        "Fertilizer",
        min_value=0.0,
        value=100.0
    )

    pesticide = st.number_input(
        "Pesticide",
        min_value=0.0,
        value=10.0
    )

    submitted = st.form_submit_button("Predict Crop Yield")


# Make the prediction
if submitted:

    input_data = pd.DataFrame([{
        "Year": int(year),
        "State": state,
        "Crop": crop,
        "Season": season,
        "Area": area,
        "Annual_Rainfall": rainfall,
        "Fertilizer": fertilizer,
        "Pesticide": pesticide
    }])

    try:
        prediction = float(model.predict(input_data)[0])

        st.subheader("Prediction Result")
        st.metric(
            "Estimated Crop Yield",
            f"{prediction:,.4f}"
        )

        with st.expander("View input details"):
            st.dataframe(input_data)

    except Exception as error:
        st.error("Prediction failed. Please check the error below.")
        st.code(str(error))

st.divider()
st.subheader("About this project")
st.write(
    "This application uses a tuned Extra Trees regression pipeline "
    "for the Crop Yield Prediction CP2 project."
)

st.caption(
    "This is an educational estimate, not a guaranteed agricultural "
    "forecast. Confirm the units and model limitations before use."
)
