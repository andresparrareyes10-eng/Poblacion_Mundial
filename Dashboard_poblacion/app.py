import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="POBLACION TOTAL", layout="wide")

st.title("Analisis de la poblacion mundial")
st.write("Aqui tenemos los 10 paises mas poblados del mundo")

archivo = st.file_uploader("Selecciona el Archivo CSV", type=["csv"])

if archivo:
    datos = pd.read_csv(archivo)
    
    # Limpiar espacios en blanco en los nombres de las columnas
    datos.columns = datos.columns.str.strip()
    
    # Buscar automáticamente las columnas por palabras clave (sin importar tildes o idioma)
    col_pais = [c for c in datos.columns if 'country' in c.lower() or 'país' in c.lower() or 'territory' in c.lower()][0]
    col_2015 = [c for c in datos.columns if '2015' in c][0]
    col_2020 = [c for c in datos.columns if '2020' in c][0]
    col_2022 = [c for c in datos.columns if '2022' in c][0]

    # Ordenar por los 10 países con mayor población en 2022
    top10 = datos.sort_values(
        col_2022,
        ascending=False
    ).head(10)

    # Convertir las columnas en arrays de NumPy
    paises = top10[col_pais].to_numpy()
    poblacion_2015 = top10[col_2015].to_numpy()
    poblacion_2020 = top10[col_2020].to_numpy()
    poblacion_2022 = top10[col_2022].to_numpy()

    # Cálculos estadísticos
    total = np.sum(poblacion_2022)
    promedio = np.mean(poblacion_2022)
    mediana = np.median(poblacion_2022)
    minimo = np.min(poblacion_2022)
    maximo = np.max(poblacion_2022)

    st.subheader("Estadisticas de la poblacion de 2022")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Poblacion Total", f"{total/1000000:,.2f} Millones")
    col2.metric("Promedio", f"{promedio/1000000:,.2f} Millones")
    col3.metric("Mediana", f"{mediana/1000000:,.2f} Millones")
    col4.metric("Minimo", f"{minimo/1000000:,.2f} Millones")
    col5.metric("Maximo", f"{maximo/1000000:,.2f} Millones")

    st.subheader("Comparacion de la poblacion por paises")

    grafico = top10.set_index(col_pais)[[
        col_2015,
        col_2020,
        col_2022
    ]] / 1000000

    st.bar_chart(grafico)

    st.subheader("Datos de los 10 paises")

    st.dataframe(top10[[
        col_pais,
        col_2015,
        col_2020,
        col_2022
    ]])

else:
    st.info("Primero descargar el dataset")