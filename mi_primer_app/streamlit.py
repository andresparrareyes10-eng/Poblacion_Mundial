import streamlit as st
import pandas as pd

st.title("Mi Primera Applicacion")
st.write("Bienvenido a mi primera aplicación con python!")
st.markdown("### Aprendiendo streamlit en visual")
st.write("Esta app muestra informacion muestra informacion de una pagina")


promedio = 4.2
st.write("el promedio es ", promedio)
datos =pd.DataFrame({
    "Estudiantes": ["Juan", "Pedro", "Maria", "Jose"],
    "Calificaciones": [4.5, 3.8, 4.9, 4.2]
})

st.dataframe(datos)

st.table(datos)

if st.button("Mostrar mensaje"):
    st.write("Boton oprimido!")

notas = st.slider("Selecciona una nota", min_value=0.0, max_value=5.0, value=3.0, step=0.1)
st.write("La nota seleccionada es: ", notas)


carrera = st.selectbox("Selecciona una sola carrera", ["Ciencia de Datos", "Sistemas", "Civil", "Arquitectura"])
st.write("La carrera seleccionada es: ", carrera)


nombre = st.text_input("Escriibe tu nombre")
if nombre:
    st.write("Hola ", nombre, " Bienvenido a la app")

archivo = st.file_uploader("Carga un archivo CSV", type=["csv",])
if archivo:
    datos=pd.read_csv(archivo)
    st.dataframe(datos)