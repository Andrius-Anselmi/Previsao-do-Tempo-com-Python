import requests
from fpdf import FPDF

def get_coordenadas(cidade):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": cidade, "count": 1, "language": "pt", "format": "json"}
    response = requests.get(url, params=params)
    data = response.json()
    if "results" not in data:
        return None
    return data["results"][0]

def get_previsao(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": ["temperature_2m_max", "temperature_2m_min"],
        "timezone": "America/Sao_Paulo",
        "forecast_days": 7
    }

    response = requests.get(url, params =params)
    return response.json()


