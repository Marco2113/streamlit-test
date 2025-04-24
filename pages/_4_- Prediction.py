# cargar el modelo ->Z pkl
# recoger el input de las X
    # o bien con un csv
    # o bien con selectores

import streamlit as st
import pickle
import pandas as pd 

st.title("Tasación")

opcion_entrada = st.radio("Selecciona opción:", ("Subir CSV", "Introducir manualmente"))
df_input = pd.DataFrame()

with open("models/modelo_entrenado.pkl", "rb") as f:
    modelo, columnas = pickle.load(f)

    if opcion_entrada == "Subir CSV":
        archivo_cargado = st.file_uploader("Subir archivo csv", type=["csv"])
        if archivo_cargado:
            df_input = pd.read_csv(archivo_cargado)
            st.dataframe(df_input)
    else:
        st.subheader("Introduce los datos del piso")
        input_data = {}
        for col in columnas:
            if col == "barrio":
                input_data[col] = st.selectbox("Barrio", ["Centro", "Norte", "Sur", "Este", "Oeste"])
                st.write(input_data)
            else:
                input_data[col] = st.number_input(col, value=0)
        df_input = pd.DataFrame([input_data])

st.dataframe(df_input)


if not df_input.empty and st.button("Predecir precio"):
        df_input = pd.get_dummies(df_input)
        for col in [c for c in modelo.feature_names_in_ if c not in df_input.columns]:
            df_input[col] = 0
        df_input = df_input[modelo.feature_names_in_]
        pred = modelo.predict(df_input)[0]
        st.success(f":moneybag: Precio estimado: {int(pred):,} €")