
import streamlit as st
from st_functions import st_button, load_css

# Cargar estilos
load_css()

AZUL = "#083b66"
AZUL_CLARO = "#7ebaf4"

# Estilo responsive para desktop vs móvil
st.markdown(
    f"""
    <style>
    .container-flex {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
    }}

    .profile-section {{
        text-align: center;
    }}

    .profile-img {{
        width: 110px;
        border-radius: 50%;
    }}

    @media (min-width: 768px) {{
        .container-flex {{
            flex-direction: row;
            align-items: flex-start;
            justify-content: center;
        }}
        .profile-section {{
            width: 50%;
            padding-right: 2rem;
        }}
        .button-section {{
            width: 50%;
            padding-left: 2rem;
        }}
        .profile-img {{
            width: 160px;
        }}
    }}

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

    </style>
    """, unsafe_allow_html=True
)

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

# Contenedor doble
st.markdown("<div class='container-flex'>", unsafe_allow_html=True)

# Columna izquierda (foto + descripción)
st.markdown("<div class='profile-section'>", unsafe_allow_html=True)
st.image(img_bytes, use_column_width=False, output_format="PNG", caption=None)
st.markdown("<h3>Hola, soy Fernando Carvajal 👋</h3>", unsafe_allow_html=True)
st.markdown(
    "<p style='background-color: #e8f4ff; padding: 10px 12px; border-radius: 10px; font-size: 13px;'>"
    "Actuario y asesor de seguros. Ayudo a personas de todas las edades a proteger lo que más importa y a construir tranquilidad financiera a través del ahorro, el retiro y la inversión."
    "</p>",
    unsafe_allow_html=True
)
st.markdown("</div>", unsafe_allow_html=True)

# Columna derecha (botones)
st.markdown("<div class='button-section'>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>📲 Conecta conmigo:</h4>", unsafe_allow_html=True)
icon_size = 20
st_button('calendar', 'https://calendly.com/fernandoa-carvajalg', 'Agendar consultoría', icon_size)
st_button('instagram', 'https://www.instagram.com/fernandocg_seguros/', 'Instagram @fernandocg_seguros', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/fernandocarvajalgomez/', 'LinkedIn profesional', icon_size)
st_button('facebook', 'https://www.facebook.com/FernandoCGSeguros', 'Facebook FernandoCGSeguros', icon_size)
st_button('youtube', 'https://www.youtube.com/@SegurosConFernando', 'YouTube Seguros con Fernando', icon_size)
st_button('cup', 'https://coff.ee/fercarvajal', 'Invítame un café ☕', icon_size)
st.markdown("</div>", unsafe_allow_html=True)

# Cierre del contenedor general
st.markdown("</div>", unsafe_allow_html=True)

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
