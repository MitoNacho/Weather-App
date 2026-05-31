# 🌤️ Weather Dashboard

Aplicación meteorológica interactiva desarrollada con **Python**, **Streamlit** y la API de **OpenWeatherMap**.

Diseñada con una interfaz moderna, fondos dinámicos según el clima y soporte visual para modo claro y oscuro.

---

## ✨ Características

✅ Consulta del clima en tiempo real

✅ Temperatura, humedad, viento y sensación térmica

✅ Fondos dinámicos según las condiciones climáticas

✅ Compatibilidad con Light Mode y Dark Mode

✅ Diseño responsive y minimalista

✅ Integración con OpenWeather API

✅ Interfaz moderna con Streamlit

---

## 📸 Vista previa

> Puedes añadir aquí capturas de pantalla de tu aplicación.

```bash
/assets/screenshot.png
```

---

## 🚀 Demo

🔗 [https://weather-app-4f3mczyqfx5zkly4cafbhk.streamlit.app/ ](https://weather-app-4f3mczyqfx5zkly4cafbhk.streamlit.app/)

---

## 🛠️ Tecnologías utilizadas

* Python
* Streamlit
* Requests
* OpenWeatherMap API
* HTML & CSS personalizado

---

## 📂 Estructura del proyecto

```bash
weather-dashboard/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── screenshot.png
│
└── utils/
    └── themes.py
```

---

## ⚙️ Instalación

### 1. Clonar repositorio

```bash

git clone https://github.com/MitoNacho/Weather-App.git

```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuración API

Crea un archivo `config.py`:

```python
API_KEY = "TU_API_KEY"
```

Puedes obtener una API key gratuita en:

[https://openweathermap.org/api](https://openweathermap.org/api)

---

## ▶️ Ejecutar aplicación

```bash
streamlit run app.py
```

---

## 🎨 Características visuales

La interfaz adapta automáticamente el fondo según el clima:

| Clima        | Fondo         |
| ------------ | ------------- |
| ☀️ Soleado   | Azul claro    |
| 🌧️ Lluvia   | Gris oscuro   |
| ❄️ Nieve     | Azul hielo    |
| 🌩️ Tormenta | Morado oscuro |
| ☁️ Nublado   | Gris suave    |

Además, los estilos se adaptan automáticamente al modo claro y oscuro del sistema.

---

## 📌 Próximas mejoras

* [ ] Pronóstico de 5 días
* [ ] Gráficas meteorológicas
* [ ] Geolocalización automática
* [ ] Historial de búsquedas
* [ ] Favoritos
* [ ] Bot de Telegram
* [ ] Dockerización

---

## 👨‍💻 Autor

Desarrollado por **Nacho Naves**

🌐 Portfolio: https://mitonacho.github.io/dev/

---

## ⭐ Support

Si te gusta este proyecto, considera darle una estrella en GitHub.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.
