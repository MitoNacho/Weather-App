import streamlit as st
import requests
from config import API_KEY

st.set_page_config(
    page_title="Mi Tiempo",
    page_icon="🌤️",
    layout="centered"
)

st.title("🌤️ Mi Tiempo")

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

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    feels_like = data["main"]["feels_like"]
    wind = data["wind"]["speed"]
    desc = data["weather"][0]["description"]

    icon = data["weather"][0]["icon"]

    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

    
    st.image(icon_url, width=100)

    st.markdown("""
<style>
                


.stApp {
    background: linear-gradient(to bottom, #87CEEB, #ffffff);
}
                

@media (prefers-color-scheme: light) {

    .stApp {
        background: linear-gradient(to bottom, #87CEEB, #ffffff);
        color: black;
    }

    h1, h2, h3, p, div, span, label {
        color: black !important;
    }
}


@media (prefers-color-scheme: dark) {

    .stApp {
        background: linear-gradient(to bottom, #0F172A, #1E293B);
        color: white;
    }

    h1, h2, h3, p, div, span, label {
        color: white !important;
    }
}

</style>
""", unsafe_allow_html=True)

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