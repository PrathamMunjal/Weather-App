import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')


@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int


def get_lat_lon(city_name, state_code, country_code, API_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data = response[0]
    lat, lon = data.get('lat'), data.get('lon')
    # print(response)
    return lat, lon
    

# get_lat_lon('Hisar', 'HR', 'India', api_key)    

def current_weather(lat, lon, API_key):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric', verify=False).json()
    data = WeatherData(
        main=response.get('weather')[0].get('main'),
        description=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        temperature=int(response.get('main').get('temp'))
    )

    return data


# print(get_lat_lon('Sirsa', 'HR', 'India', api_key))


def main(city_name, state_code, country_code):
    lat, lon = get_lat_lon(city_name, state_code,country_code, api_key)
    weather_data = current_weather(lat, lon, api_key)
    return weather_data



if __name__ == "__main__":
    
    print(current_weather(lat, lon, api_key))