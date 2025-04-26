import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter your height (in cm):", 100, 250, 175)
weigth = st.slider("Enter your weight (in Kg)", 40, 200, 70)

bmi = weigth / ((height/100) ** 2)

st.write(f"Your BMI is {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("_Underweight: BMI less than 18.5")
st.write("_Normal weight: BMI between 18.5and 24.9")
st.write("_ Overweight: BMI between 18.5 and 29.9")
st.write("_ Obesity: BMI 30 or greater")



