from bs4 import BeautifulSoup
import requests
from text import weather_error_string
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def warnings(temperature, environment):
    HIGH = 25
    LOW = 0
    if temperature >= HIGH:
        return "Remember to drink water frequently to avoid heatstroke!"
    elif temperature <= LOW:
        return "Remember to dress warmly!"
    if "rain" in environment or "snow" in environment:
        return "The roads may be slippery. Exercise caution when driving!"
    elif "sunny" in environment:
        return "Be careful to avoid sunburn!"
    return""

def format_url(city):
    city = city+" weather"
    city = city.replace(" ", "+")
    return "https://www.google.com/search?q=" + city + "&oq=" + city

def weather_city(city):
    url = format_url(city)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    catch = soup.select('#wob_loc')
    if(not catch):
        return weather_error_string
    location = soup.select('#wob_loc')[0].getText().strip()
    # time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    temperature = soup.select('#wob_tm')[0].getText().strip()
    msg = warnings(int(temperature), info)
    retval = f"City: {location}\nWeather: {info}\nTemperature: {temperature}°C\n{msg}\n"
    return retval
# print(weather_city("Milton"))