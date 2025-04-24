# 1.Creamos entorno
mkdir streamlit.test
pipenv shell
python = 3.10
pip install streamlit

# 2. Creado archivo app
touch app.py

# 3. Streamlit
pip instal streamlit
streamlit run app.py

# 4. Generar archivos de requirements.txt
pip install pipreqs
pipreqs

# 5. Dependencias

pip install plotly
pip install folium
pip install streamlit_folium
pip install scikit-learn

# NOTAS
- Para parar el servidor "Ctrl + C"

# EXTRA
- *args: numero de variable argumentos
-**kwargs: número variable keyword arguments