import streamlit as st
import pandas as pd

st.title("Sistema de Calificaciones")
st.write("consulte y registre las materias ")

st.markdown("###mis materias con sus respectivas notas")

datos = {
    "materia":["logica","intduccion","filosofia","algebra","calculo"],
    "calificacion":[2.0,2.1,4.5,4.5,3.0]
}

tabla = pd.DataFrame(datos)
st.dataframe(tabla)

promedio = tabla["calificacion"].mean()
st.write("el promedio es ", round(promedio,2))

nueva_materia = st.text_input("Ingrese el nombre de la materia")
nueva_calificacion = st.slider("Ingrese la calificacion de la materia", min_value=0.0, max_value=5.0, value=3.0, step=0.1)
if st.button("Agregar materia"):
    if nueva_materia != "":
        materia= {"materia": nueva_materia, "calificacion": nueva_calificacion}

    nueva_fila = pd.DataFrame([materia])
    nueva_tabla = pd.concat([tabla, nueva_fila], ignore_index=True)

    st.success("Materia agregada correctamente!")
    st.dataframe(nueva_tabla)

    promedio= nueva_tabla["calificacion"].mean()
    st.write("el promedio es ", round(promedio,2))
else:
    st.warning("Por favor ingrese el nombre de la materia")
