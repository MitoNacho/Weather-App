import streamlit as st
import requests
from config import API_KEY

def get_background(weather_main):

    weather_main = weather_main.lower()

    themes = {

        "clear": {
            "light": "linear-gradient(to bottom, #87CEEB, #ffffff)",
            "dark": "linear-gradient(to bottom, #0F172A, #1E3A8A)"
        },

        "rain": {
            "light": "linear-gradient(to bottom, #6B7280, #D1D5DB)",
            "dark": "linear-gradient(to bottom, #111827, #374151)"
        },

        "snow": {
            "light": "linear-gradient(to bottom, #E0F2FE, #FFFFFF)",
            "dark": "linear-gradient(to bottom, #1E293B, #475569)"
        },

        "thunderstorm": {
            "light": "linear-gradient(to bottom, #7C3AED, #C4B5FD)",
            "dark": "linear-gradient(to bottom, #2E1065, #4C1D95)"
        },

        "clouds": {
            "light": "linear-gradient(to bottom, #CBD5E1, #F8FAFC)",
            "dark": "linear-gradient(to bottom, #1E293B, #334155)"
        }
    }

    return themes.get(
        weather_main,
        {
            "light": "linear-gradient(to bottom, #87CEEB, #ffffff)",
            "dark": "linear-gradient(to bottom, #0F172A, #1E293B)"
        }
    )



st.set_page_config(
    page_title="Mi Tiempo con Python",
    page_icon="🌤️",
    layout="centered"
)

st.title("🌤️ Mi Tiempo")

st.markdown("""
<style>

.portfolio-banner {
    padding: 1.2rem;
    border-radius: 18px;
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(12px);
    text-align: center;
    margin-bottom: 25px;
    border: 1px solid rgba(255,255,255,0.15);
}

.portfolio-btn {
    display: inline-block;
    margin-top: 10px;
    padding: 12px 24px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: bold;
    transition: all 0.3s ease;
    background: #2563EB;
    color: white !important;
}

.portfolio-btn:hover {
    transform: scale(1.05);
    background: #1D4ED8;
}

</style>

<div class="portfolio-banner">            
    <h3 style="margin-bottom: 10px;">
    👨‍💻 Proyecto desarrollado por Nacho Naves 
    </h3>

<a href="https://mitonacho.github.io/dev/" target="_blank">
            <div class="portfolio-btn">
            <button style="
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 10px;
        cursor: pointer;
        font-size: 16px;
        transition: 0.3s;
    ">
        Ver Portfolio 🚀
    </button>
</a>

</div>
</>            
""", unsafe_allow_html=True)



city = st.text_input(
    "Introduce una ciudad",
    placeholder="Ejemplo: Madrid"
)

if city:

    city = city.strip()

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
        f"&lang=es"
    )

    with st.spinner("Buscando clima..."):

        response = requests.get(url)

    if response.status_code != 200:
        st.error("❌ Ciudad no encontrada")
        st.stop()
    

    

    
    data = response.json()
    weather_main = data["weather"][0]["main"]

    

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    feels_like = data["main"]["feels_like"]
    wind = data["wind"]["speed"]
    desc = data["weather"][0]["description"]

    bg = get_background(weather_main)

    icon = data["weather"][0]["icon"]

    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

    
    st.image(icon_url, width=100)

    st.markdown(
    f"""
    <style>

    
    @media (prefers-color-scheme: light) {{

        .stApp {{
            background: {bg["light"]};
            color: black;
        }}

        h1, h2, h3, p, div, span, label {{
            color: black !important;
        }}
    }}

    
    @media (prefers-color-scheme: dark) {{

        .stApp {{
            background: {bg["dark"]};
            color: white;
        }}

        h1, h2, h3, p, div, span, label {{
            color: white !important;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True
)

    st.subheader(desc.capitalize())

    col1, col2 = st.columns(2)

    with col1:
        st.metric("🌡️ Temperatura", f"{temp}°C")

    with col2:
        st.metric("🤒 Sensación", f"{feels_like}°C")

    col3, col4 = st.columns(2)

    with col3:
        st.metric("💧 Humedad", f"{humidity}%")

    with col4:
        st.metric("💨 Viento", f"{wind} m/s")

else:
    st.info("Escribe una ciudad para consultar el clima")




