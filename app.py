import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tasador" , page_icon="🏠", layout="wide")
st.title("🏠Prediccion de Pisos")
st.write("Tasador de pisos en Madrid")


tab1, tab2 = st.tabs(["Resumen", "Contacto"])
with tab1:
    st.subheader("Resumen del proyecto")
    st.write("Este es un proyecto de predicción de precios de pisos en Madrid.")

with tab2:
    st.subheader("Contacto")
    st.write("Autor: Marco Adrian")
    st.write("Madrid, España")

