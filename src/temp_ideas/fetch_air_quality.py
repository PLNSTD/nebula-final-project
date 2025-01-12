import fetch_data.fetch_webpage as fw
import temp_ideas.OpenWeatherAPIKey as api_key


def fetch_city_air_quality(city):
    common_city = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key.get_key()}'
    data = fw.fetch_page_content(common_city).json()
    lon, lat = data["coord"]["lon"], data["coord"]["lat"]

    air_pollution_url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key.get_key()}'
    print(air_pollution_url)
    data = fw.fetch_page_content(air_pollution_url).json()
    aqi = data["list"][0]["main"]["aqi"]

    return aqi