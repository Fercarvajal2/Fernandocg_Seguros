
import streamlit as st

def load_css():
    st.markdown("""
        <style>
        .link-button-container {
            display: flex;
            justify-content: center;
            margin: 10px 0;
        }
        .link-button {
            background-color: #7ebaf4;
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 10px;
            font-weight: 600;
            font-size: 16px;
            display: inline-block;
            width: 100%;
            max-width: 400px;
            text-align: center;
            transition: background-color 0.3s ease;
            border: none;
        }
        .link-button:hover {
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
        "cup": "🍎",
        "whatsapp": "💬",
        "calendar": "📅"
    }
    icon = icons.get(icon_name, "")
    st.markdown(
        f"""
        <div class="link-button-container">
            <a class="link-button" href="{url}" target="_blank">{icon} {label}</a>
        </div>
        """, unsafe_allow_html=True
    )
