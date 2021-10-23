from pyowm.owm import OWM
import pandas as pd
from datetime import datetime
import keys

owm = OWM(keys.owm_token)
reg = owm.city_id_registry()
mgr = owm.weather_manager()


def get_current_weather(lat, lng):
    observation = mgr.weather_at_coords(lat, lng)
    w = observation.weather
    now = datetime.now()

    print(f'humidity {w.humidity}\n'
          f'pressure: {w.pressure["press"]}\n'
          f'tempC: {w.temperature("celsius")["temp"]}\n'
          f'windspeedKmph: {w.wind()["speed"]}\n'
          f'year: {now.year}\n'
          f'day: {now.day}\n'
          f'hour: {now.hour}\n'
          f'lat: {lat}\n'
          f'lng: {lng}')

    data = {'humidity': [w.humidity],
            'pressure': [w.pressure["press"]],
            'tempC': [w.temperature("celsius")["temp"]],
            'windspeedKmph': [w.wind()["speed"]],
            'year': [now.year],
            'day': [now.day],
            'hour': [now.hour],
            'lat': [lat],
            'lng': [lng]}

    df = pd.DataFrame(data, columns=['humidity', 'pressure', 'tempC',
                                     'windspeedKmph', 'year', 'day',
                                     'hour', 'lat', 'lng'])

    return df
