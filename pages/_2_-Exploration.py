import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Exploración interactiva")

df = pd.read_csv("data/pisos.csv")
st.dataframe(df)

st.sidebar.header("Filtros")

# 1. Input
barrios = st.sidebar.multiselect("Barrio", df["barrio"].unique())

precio_min, precio_max = df["precio"].min(), df["precio"].max()
price_range = st.sidebar.slider("Precio", precio_min, precio_max, (precio_min, precio_max))

habitaciones = st.sidebar.slider("Habitaciones", df["habitaciones"].min(), df["habitaciones"].max(), (df["habitaciones"].min(), df["habitaciones"].max()))

# 2. Filtrado
df_filtrado = df[
    (df["barrio"].isin(barrios)) & 
    (df["precio"].between(price_range[0], price_range[1])) & 
    (df["habitaciones"].between(habitaciones[0], habitaciones[1]))
]

st.write("Tus resultados: ")
st.dataframe(df_filtrado)

st.subheader("Histograma de precios")
st.plotly_chart(px.histogram(df_filtrado, x="precio"))

st.subheader("Boxplot por barrio")
st.plotly_chart(px.box(df_filtrado, x="barrio", y="precio"))