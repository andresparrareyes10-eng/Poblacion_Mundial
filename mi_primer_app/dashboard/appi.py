import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Deportivo", layout="centered")

st.title("panel de rendimiento: Equipo Datos Santoto")
st.write("Estadisticas clave de los jugadores en el semestre actual")

datos={
    "Jugador":["sebastian","manuel","cristian","gabriela"],
    "Goles":[10,14,20,1],
    "Asistencias":[5,7,10,3],
}
df=pd.DataFrame(datos)
col1,col2,col3,col4=st.columns(4)

col1.metric("Goles totales",df["Goles"].sum())
col2.metric("Asistencias totales",df["Asistencias"].sum())
col3.metric("Goleador del Equipo",df.loc[df["Goles"].idxmax(), "Jugador"])
col4.metric("Posicion de liga del equipo", value="3°", delta="-1°")


st.subheader("Estadisticas al detalle")
st.dataframe(df)

st.subheader("Comparativa de rendiemiento")
st.bar_chart(df.set_index("Jugador"))