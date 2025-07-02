
import streamlit as st
from st_functions import st_button, load_css

# Cargar estilos
load_css()

# Colores de tu paleta
AZUL = "#083b66"
AZUL_CLARO = "#7ebaf4"

# Encabezado principal optimizado para móvil
st.markdown(
    f"""
    <div style='text-align: center; background-color: {AZUL}; padding: 1rem; border-radius: 15px;'>
        <h1 style='color: white; font-size: 22px; margin-bottom: 4px;'>Seguros con Fernando</h1>
        <p style='color: {AZUL_CLARO}; font-size: 14px; margin: 0;'>Protege tu presente, construye tu futuro</p>
    </div>
    """, unsafe_allow_html=True
)

# Estilo para imagen más compacto
st.markdown(
    "<style>img { max-width: 180px !important; border-radius: 50%; margin: 10px auto; display: block; }</style>",
    unsafe_allow_html=True
)

# Imagen central (logo o perfil)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    with open("dp.png", "rb") as file:
        img_bytes = file.read()
    st.image(img_bytes, use_column_width=True)

# Presentación centrada
st.markdown("<h3 style='text-align: center;'>Hola, soy Fernando Carvajal 👋</h3>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; background-color: #e8f4ff; padding: 10px; border-radius: 10px;'>"
    "Actuario y asesor de seguros. Ayudo a personas de todas las edades a proteger lo que más importa y a construir tranquilidad financiera a través del ahorro, el retiro y la inversión."
    "</p>",
    unsafe_allow_html=True
)

# Redes sociales actualizadas
st.markdown("<h4 style='text-align: center;'>📲 Conecta conmigo:</h4>", unsafe_allow_html=True)
icon_size = 20
st_button('calendar', 'https://calendly.com/fernandoa-carvajalg', 'Agendar consultoría', icon_size)
st_button('instagram', 'https://www.instagram.com/fernandocg_seguros/', 'Instagram @fernandocg_seguros', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/fernandocarvajalgomez/', 'LinkedIn profesional', icon_size)
st_button('facebook', 'https://www.facebook.com/FernandoCGSeguros', 'Facebook FernandoCGSeguros', icon_size)
st_button('youtube', 'https://www.youtube.com/@SegurosConFernando', 'YouTube Seguros con Fernando', icon_size)
st_button('cup', 'https://coff.ee/fercarvajal', 'Invítame a una Manzana 🍎', icon_size)

# Frase de cierre centrada
st.markdown(
    f"""
    <hr>
    <p style='text-align: center; color:{AZUL}; font-size: 16px;'>
    ¿Listo para comenzar a construir tu tranquilidad financiera? <br>
    Agenda tu espacio y empecemos.
    </p>
    """, unsafe_allow_html=True
)
