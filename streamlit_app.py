
import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

# Cargar estilos
load_css()

# Colores de tu paleta
AZUL = "#083b66"
BEIGE = "#f5f1ec"
AZUL_CLARO = "#7ebaf4"

# Encabezado principal
st.markdown(
    f"""
    <div style='text-align: center; background-color: {AZUL}; padding: 1.5rem; border-radius: 15px;'>
        <h1 style='color: white;'>Seguros con Fernando</h1>
        <p style='color: {AZUL_CLARO}; font-size: 18px; font-style: italic;'>Protege tu presente, construye tu futuro</p>
    </div>
    """, unsafe_allow_html=True
)

# Imagen central (logo o perfil)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(Image.open("dp.png"), use_column_width=True)

# Presentación
st.markdown("### Hola, soy Fernando Carvajal 👋")
st.info("Actuario y asesor de seguros. Ayudo a personas de todas las edades a proteger lo que más importa y a construir tranquilidad financiera a través del ahorro, el retiro y la prevención.")

# Redes sociales actualizadas
st.markdown("#### 📲 Conecta conmigo:")
icon_size = 20
st_button('whatsapp', 'https://wa.me/5219996004456', 'Escríbeme por WhatsApp', icon_size)
st_button('instagram', 'https://www.instagram.com/fernandocg_seguros/', 'Instagram @fernandocg_seguros', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/fernandocarvajalgomez/', 'LinkedIn profesional', icon_size)
st_button('facebook', 'https://www.facebook.com/FernandoCGSeguros', 'Facebook FernandoCGSeguros', icon_size)
st_button('youtube', 'https://www.youtube.com/@SegurosConFernando', 'YouTube Seguros con Fernando', icon_size)
st_button('cup', 'https://coff.ee/fercarvajal', 'Invítame un café ☕', icon_size)

# Calendario
st.markdown("#### 📅 ¿Qué publico cada semana?")
st.markdown("""
- **Lunes**: Video corto (ahorro, PPR, seguros)
- **Miércoles**: Infografía o carrusel (tips, errores comunes, comparativos)
- **Viernes**: Historia real de algún cliente (vida real, emergencias, aprendizaje)
""")

# Frase de cierre
st.markdown(
    f"""
    <hr>
    <p style='text-align:center; color:{AZUL}; font-size: 16px;'>
    ¿Listo para comenzar a construir tu tranquilidad financiera? <br>
    Estoy aquí para ayudarte.
    </p>
    """, unsafe_allow_html=True
)
