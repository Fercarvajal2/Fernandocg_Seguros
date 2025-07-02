
import streamlit as st

def load_css():
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #7ebaf4;
            color: white;
            padding: 8px 16px;
            border-radius: 8px;
            border: none;
            font-weight: bold;
            margin: 4px 0;
        }
        .stButton>button:hover {
            background-color: #083b66;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

def st_button(icon_name, url, label, icon_size=20):
    icons = {
        "youtube": "📺",
        "linkedin": "💼",
        "instagram": "📷",
        "facebook": "📘",
        "medium": "✍️",
        "twitter": "🐦",
        "newsletter": "📬",
        "cup": "☕",
        "whatsapp": "💬"
    }
    icon = icons.get(icon_name, "")
    st.markdown(
        f'<a href="{url}" target="_blank">'
        f'<button style="font-size:{icon_size}px">{icon} {label}</button>'
        f'</a>',
        unsafe_allow_html=True
    )
