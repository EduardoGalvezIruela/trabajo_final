import streamlit as st
import time

st.set_page_config(page_title='Práctica Final', layout='wide',     page_icon="📈")
st.image('foto.jpg') 

placeholder = st.empty()
with placeholder:
    #from PIL import Image
    #image = Image.open('mired.png')
    #placeholder.image(image, caption='MiRed semantic engine',use_column_width = 'always') 
    for seconds in range(5):
        placeholder.write(f"⏳ {seconds} Cargando página")
        time.sleep(1)
placeholder.empty()


st.title("Bienvenido a mi práctica final")

st.sidebar.success("Selecciona la página que desees.")

st.markdown(
    """
    Este es el trabajo final de la asignatura Programación II, realizado por Eduardo Gálvez Iruela.
    Se trata de una plataforma interactiva desarrollada en Streamlit que permite la visualización y 
    análisis de datos relacionados con los 2640 individuos más ricos a nivel mundial, conforme a la 
    clasificación elaborada por la revista Forbes. Este dataset proporciona una visión detallada de la distribución 
    de la riqueza, los sectores empresariales, y diversos detalles personales de los individuos más ricos 
    del mundo.

    Para conocer más detalles, visitar el repositorio de github y leer el archivo README.md

    Espero que os guste!
"""
)

st.title("¿Qué es y cómo salir en la revista Forbes?")
st.video("video.mp4")