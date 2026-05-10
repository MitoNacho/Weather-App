import streamlit as st
import requests
import urllib.parse
from config import API_KEY


st.title("🌤️ Mi Tiempo")

city = st.text_input("Escribe una ciudad")

if not city:
    st.info("Escribe una ciudad para ver el clima")
    st.stop()

if city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if "main" in data:
        temp = data["main"]["temp"]
        st.write(f"Temperatura: {temp}°C")
    else:
        st.error("No se encontraron datos del clima")

city_encoded = urllib.parse.quote(city)

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es"

response = requests.get(url)
if response.status_code != 200:
    st.error("Introduce una ciudad válida")
    st.stop()

data = response.json()
if "main" not in data:
    st.error("Datos incompletos de la API")
    st.stop()

temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
feels_like = data["main"]["feels_like"]
wind = data["wind"]["speed"]
desc = data["weather"][0]["description"]

st.write(f"🌡️ Temperatura: {temp}°C")
st.write(f"🤒 Sensación: {feels_like}°C")
st.write(f"💧 Humedad: {humidity}%")
st.write(f"💨 Viento: {wind} m/s")
st.write(f"☁️ Estado: {desc}")