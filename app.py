from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator
from streamlit_lottie import st_lottie
import json

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Patrick+Hand&display=swap');

.stApp {
    background-color: #FFFDF6;
    background-image:
        linear-gradient(90deg, transparent 68px, #E8B4B8 68px, #E8B4B8 70px, transparent 70px),
        repeating-linear-gradient(180deg, transparent 0px, transparent 33px, #CFE0E8 33px, #CFE0E8 34px);
    background-size: 100% 100%, 100% 34px;
}

h1, h2, h3 {
    font-family: 'Caveat', cursive !important;
    color: #4A3F35 !important;
    font-size: 2.4rem !important;
}
h2 { font-size: 1.7rem !important; }
h3 { font-size: 1.4rem !important; }

p, li, label, div[data-testid="stMarkdownContainer"], .stMarkdown {
    font-family: 'Patrick Hand', cursive !important;
    font-size: 1.2rem !important;
    color: #4A3F35 !important;
}

section[data-testid="stSidebar"] {
    background-color: #FBF3E7;
    border-right: 2px dashed #D9BFA9;
}

div[data-testid="stImage"] img {
    border-radius: 10px;
    box-shadow: 3px 3px 10px rgba(0,0,0,0.15);
    transform: rotate(-1deg);
}

div[data-testid="stExpander"] {
    background-color: #FFFBF0;
    border: 1.5px solid #D9BFA9 !important;
    border-radius: 10px;
}

div[data-testid="stAlert"] {
    font-family: 'Patrick Hand', cursive !important;
    background-color: #FBF3E7 !important;
    border-left: 4px solid #A9CBA4 !important;
}

input, .stTextInput input {
    font-family: 'Patrick Hand', cursive !important;
    font-size: 1.2rem !important;
    background-color: transparent !important;
    border: none !important;
    border-bottom: 2px solid #A9CBA4 !important;
    border-radius: 0 !important;
    color: #4A3F35 !important;
}
</style>
""", unsafe_allow_html=True)

st.title('Mi Diario de Reflexión')
image = Image.open('emoticones.png')
st.image(image)
st.subheader("Escribe cómo te fue hoy o cómo te sientes sobre algo, y descubre el tono de tus palabras")

st.info(
    "ℹ️ Esto analiza el texto que escribes con procesamiento de lenguaje natural (polaridad y subjetividad), "
    "no interpreta cómo te sientes realmente. Es una guía de reflexión, no un diagnóstico ni una herramienta "
    "clínica, y no reemplaza el acompañamiento de un profesional de salud mental."
)

translator = Translator()

with st.sidebar:
               st.subheader("¿Qué significan estos números?")
               ("""
                Polaridad: indica si el tono de lo que escribiste es positivo, negativo o neutral.
                Va de -1 (muy negativo) a 1 (muy positivo), con 0 como neutral.

                Subjetividad: mide qué tanto de tu texto son opiniones o emociones frente a hechos objetivos.
                Va de 0 (objetivo) a 1 (subjetivo).

                 """
               ) 

with st.expander('Escribir una entrada'):
    text = st.text_input('¿Cómo te sientes hoy? ')
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('Polaridad: ', round(blob.sentiment.polarity,2))
        st.write('Subjetividad: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x > 0.0:
            st.write( 'Tu entrada suena positiva 😊')
            with open ('happyP.json') as source:
              animation = json.load (source)
            st.lottie(animation, width=350)
        elif x < 0.0:
            st.write( 'Tu entrada suena negativa 😔')
            with open ('sadM.json') as source:
              animation = json.load (source)
            st.lottie(animation, width=350)          
        else:
            st.write( 'Tu entrada suena neutral 😐')
            with open ('NeutralE.json') as source:
              animation = json.load (source)
            st.lottie(animation, width=350)
