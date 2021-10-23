from pyowm.owm import OWM
import pandas as pd
from datetime import datetime
import keys

owm = OWM(keys.owm_token)
mgr = owm.weather_manager()


def get_current_weather(lat, lng):
    observation = mgr.weather_at_coords(lat, lng)
    w = observation.weather
    now = datetime.now()

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
