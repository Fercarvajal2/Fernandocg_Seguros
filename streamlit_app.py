
import streamlit as st
from st_functions import st_button, load_css

# Cargar estilos
load_css()

# Colores
AZUL = "#083b66"
AZUL_CLARO = "#7ebaf4"

# Header compacto
st.markdown(
    f"""
    <div style='text-align: center; background-color: {AZUL}; padding: 0.8rem; border-radius: 15px;'>
        <h1 style='color: white; font-size: 20px; margin-bottom: 4px;'>Seguros con Fernando</h1>
        <p style='color: {AZUL_CLARO}; font-size: 13px; margin: 0;'>Protege tu presente, construye tu futuro</p>
    </div>
    """, unsafe_allow_html=True
)

# Estilo para imagen reducida
st.markdown(
    """
    <style>
    .profile-pic-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0.5rem 0 0.3rem 0;
    }
    .profile-pic-container img {
        max-width: 110px !important;
        border-radius: 50%;
    }
    </style>
    """, unsafe_allow_html=True
)

# Imagen centrada
with open("dp.png", "rb") as file:
    img_bytes = file.read()
st.markdown("<div class='profile-pic-container'>", unsafe_allow_html=True)
st.image(img_bytes)
st.markdown("</div>", unsafe_allow_html=True)

# Presentación más compacta
st.markdown("<h3 style='text-align: center; font-size: 17px;'>Hola, soy Fernando Carvajal 👋</h3>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; background-color: #e8f4ff; padding: 8px 12px; border-radius: 10px; font-size: 13px;'>"
    "Actuario y asesor de seguros. Ayudo a personas de todas las edades a proteger lo que más importa y a construir tranquilidad financiera a través del ahorro, el retiro y la inversión."
    "</p>",
    unsafe_allow_html=True
)

# Botones
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
