"""
Desafio 1 - Integração com serviços de terceiros
Acesse o site do OpenWeatherMap, faça login e familiarize-se com a API.
Desenvolva um código em Python que consuma a API do OpenWeatherMap.
Implemente tratamento de erros para chamadas mal-sucedidas à API.
Extraia os dados retornados e salve-os em um arquivo de sua escolha (CSV, XLSX, XML, PDF,
HTML, etc.).
"""
import pandas as pd
import requests
import os
from dotenv import load_dotenv


# carregar o .env para poder acessar a api_key
load_dotenv()

# API Key do OpenWeather
API_KEY = os.getenv('API_KEY_OPENWEATHER')

# URL para as chamadas
base_url = 'http://api.openweathermap.org/data/2.5/weather'

# função para fazer a requisição à API para obter dados da cidade escolhida
def get_weather_data(city_name):
    params = {
        'appid': API_KEY,
        'q': city_name,
        'units': 'metric',
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()                          #Mostra respostas não sucedidas
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

    except Exception as err:
        print(f'Other error occurred: {err}')

    return None

# função para salvar os dados num arquivo CSV
def save_to_csv(data, filename='weather.csv'):
    if data:
        weather_df = pd.DataFrame([data])
        weather_df.to_csv(filename, index=False)
        print(f'Dados de {data["Cidade"]} salvos em {filename}')

    else:
        print(f'Sem dados para salvar')


if __name__ == '__main__':
    city = input('Informe o nome da cidade: ')
    weather_data = get_weather_data(city)

    if weather_data:
        weather_info = {
            "Cidade": city,
            "Temperatura": str(weather_data["main"]["temp"])+"°C",
            "Umidade": str(weather_data["main"]["humidity"])+"%",
            "Pressão": str(weather_data["main"]["pressure"])+" hPa",
            "Descrição": weather_data["weather"][0]["description"],
        }
        for line in weather_info:
            print(f'{line}: {weather_info[line]}')

        save_to_csv(weather_info)

    else:
        print(f'Sem dados para salvar')