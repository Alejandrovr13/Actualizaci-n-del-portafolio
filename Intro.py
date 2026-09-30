import streamlit as st
from PIL import Image

st.title("Portafolio De Alejandro Vizcaino Restrepo.")

with st.sidebar:
    st.subheader("Estudiante: Alejandro Vizcaino Restrepo.")
    parrafo = (
        "Aqui podremos ver las diferentes clases vistas en la materia de Programacion Avanzada"
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Vectores y Matrices")
    image = Image.open("txt_to_audio2.png")
    st.image(image, width=190)
    url = "https://clase12-08-fixhnxkn7waimszlkdn93c.streamlit.app/"
    st.write(f"[Enlace]({url})")

    st.subheader("Preparacion de Datos")
    image = Image.open("OIG5.jpg")
    st.image(image, width=200)
    url = "https://clase19-08-89dkkyt4nu4vtzjfbdtnjv.streamlit.app/"
    st.write(f" [Enlace]({url})")

    st.subheader("Gradiantes")
    image = Image.open("OIG5.jpg")
    st.image(image, width=200)
    url = "https://clase24-08-xcofsjgyx2jhyt6onheq36.streamlit.app/"
    st.write(f" [Enlace]({url})")

with col2:
    st.subheader("Lógica, Big-O y Vectorización")
    image = Image.open("OIG8.jpg")
    st.image(image, width=200)
    url = "https://clase26-08-nlmunfuth36gg8tqppnf8x.streamlit.app/"
    st.write(f" [Enlace]({url})")

    st.subheader("Preparación de datos")
    image = Image.open("data_analisis.png")
    st.image(image, width=190)
    url = "https://clase31-08-8wly2hgh8wuc3a8s7awyry.streamlit.app/"
    st.write(f" [Enlace]({url})")

    st.subheader("Preparación de datos")
    image = Image.open("OIG3.jpg")
    st.image(image, width=200)
    url = "https://clase02-09-byeepnhmiwzhj92y72a4rz.streamlit.app/"
    st.write(f" [Enlace]({url})")
    
with col3:
    st.subheader("Regresión Lineal.")
    image = Image.open("Chat_pdf.png")
    st.image(image, width=190)
    url = "https://chatpdf-cc.streamlit.app/"
    st.write(f" [Enlace]({url})")

   st.subheader("Series de Tiempo.")
    image = Image.open("Chat_pdf.png")
    st.image(image, width=190)
    url = "https://chatpdf-cc.streamlit.app/"
    st.write(f" [Enlace]({url})")

    st.subheader("Sistema de IoT Captura de datos y procesamiento.") 
    image = Image.open("Chat_pdf.png")
    st.image(image, width=190)}
    url = "https://chatpdf-cc.streamlit.app/"
    st.write(f" [Enlace]({url})")

