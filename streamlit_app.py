
import streamlit as st
from st_functions import st_button, load_css

load_css()

AZUL = "#083b66"
AZUL_CLARO = "#7ebaf4"

# Estilos generales
st.markdown(f"""
    <style>
    .card {{
        background-color: {AZUL};
        color: white;
        padding: 1rem;
        text-align: center;
        border-radius: 15px;
        margin-bottom: 1rem;
    }}
    .subtitle {{
        color: {AZUL_CLARO};
        font-size: 13px;
        margin: 0;
    }}
    .profile-pic {{
        display: block;
        margin: 0 auto 1rem auto;
        width: 120px;
        border-radius: 50%;
    }}
    @media (min-width: 768px) {{
        .profile-pic {{
            width: 140px;
        }}
    }}
    .bio {{
        background-color: #e8f4ff;
        padding: 12px;
        border-radius: 10px;
        font-size: 13px;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# Encabezado
st.markdown(
    f"""
    <div class='card'>
        <h1 style='font-size: 20px; margin-bottom: 4px;'>Seguros con Fernando</h1>
        <p class='subtitle'>Protege tu presente, construye tu futuro</p>
    </div>
    """, unsafe_allow_html=True
)

# Imagen
with open("dp.png", "rb") as file:
    img_bytes = file.read()
st.image(img_bytes, use_column_width=False, output_format="PNG", caption=None)

# Nombre y bio
st.markdown("<h3 style='text-align: center; font-size: 18px;'>Hola, soy Fernando Carvajal 👋</h3>", unsafe_allow_html=True)
st.markdown(
    "<div class='bio'>"
    "Actuario y asesor de seguros. Ayudo a personas de todas las edades a proteger lo que más importa y a construir tranquilidad financiera a través del ahorro, el retiro y la inversión."
    "</div>",
    unsafe_allow_html=True
)

# Botones sociales
st.markdown("<h4 style='text-align: center;'>📲 Conecta conmigo:</h4>", unsafe_allow_html=True)
icon_size = 20
st_button('calendar', 'https://calendly.com/fernandoa-carvajalg', 'Agendar consultoría', icon_size)
st_button('instagram', 'https://www.instagram.com/fernandocg_seguros/', 'Instagram @fernandocg_seguros', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/fernandocarvajalgomez/', 'LinkedIn profesional', icon_size)
st_button('facebook', 'https://www.facebook.com/FernandoCGSeguros', 'Facebook FernandoCGSeguros', icon_size)
st_button('youtube', 'https://www.youtube.com/@SegurosConFernando', 'YouTube Seguros con Fernando', icon_size)
st_button('cup', 'https://coff.ee/fercarvajal', 'Invítame un café ☕', icon_size)

# Cierre
st.markdown(
    f"""
    <hr>
    <p style='text-align: center; color:{AZUL}; font-size: 14px;'>
    ¿Listo para comenzar a construir tu tranquilidad financiera?<br>
    Agenda tu espacio y empecemos.
    </p>
    """, unsafe_allow_html=True
)
