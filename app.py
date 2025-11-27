import streamlit as st
import pandas as pd
import pickle

# ---------------------------
# Load the trained model
# ---------------------------
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

st.title("🏡 House Price Prediction App")
st.write("Fill in the details below to predict the house price.")

# ---------------------------
# Input Fields
# ---------------------------

area = st.number_input("Area (sq ft)", min_value=0.0, step=50.0)

bedrooms = st.number_input("Bedrooms", min_value=0, step=1)
bathrooms = st.number_input("Bathrooms", min_value=0, step=1)
stories = st.number_input("Stories", min_value=0, step=1)

mainroad = st.selectbox("Main Road Access", ["Yes", "No"])
guestroom = st.selectbox("Guest Room", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
parking = st.number_input("Parking Spaces", min_value=0, step=1)
prefarea = st.selectbox("Preferred Area", ["Yes", "No"])

# Convert Yes/No to 1/0
def encode(val):
    return 1 if val == "Yes" else 0

data = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "stories": [stories],
    "mainroad": [encode(mainroad)],
    "guestroom": [encode(guestroom)],
    "basement": [encode(basement)],
    "hotwaterheating": [encode(hotwaterheating)],
    "airconditioning": [encode(airconditioning)],
    "parking": [parking],
    "prefarea": [encode(prefarea)]
})

# ---------------------------
# Predict Button
# ---------------------------
if st.button("Predict Price"):
    price = model.predict(data)[0]
    st.success(f"Predicted House Price: **₦{price:,.2f}**")
