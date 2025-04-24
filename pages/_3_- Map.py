import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

data = pd.read_csv("data/pisos.csv")
centro = [data["lat"].mean(), data["lon"].mean()]

# 1. Mapa
m = folium.Map(location=centro, zoom_start=13)

# 2. Icono
icon = folium.Icon(icon="igloo", prefix="fa", color="blue")

# 3. Marker
def add_marker_to_map (fila):
    color = "blue"

    if fila["barrio"] == "Centro":
        color = "black"

    icon = folium.Icon(icon="igloo", prefix="fa", color=color)

    marker = folium.Marker(
        location=(fila['lat'], fila['lon']),
        popup=f"{fila['barrio']} - {fila['precio']} €",
        icon=icon
    )
    marker.add_to(m)

# 4. Iterar por el csv: para añadir cada fila como un marcador nuevo
for index, row in data.iterrows():
    add_marker_to_map (row)

st_folium(m, width = 800, height=600)
