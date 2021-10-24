from pyowm.owm import OWM
import pandas as pd
import datetime
from datetime import datetime, timedelta
import keys


# Initing OWM
owm = OWM(keys.owm_token)
mgr = owm.weather_manager()


def get_current_weather(lat: float, lng: float) -> pd.DataFrame:  # Is this marker correct?
    global mgr
    observation = mgr.weather_at_coords(lat, lng)
    w = observation.weather
    now = datetime.datetime.now()

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


def get_three_days_weather(lat: float, lng: float) -> pd.DataFrame:  # Is this marker correct?

    global mgr
    one_call = mgr.one_call(lat, lng)
    starting_time = datetime.now()

    data = {'humidity': [],
            'pressure': [],
            'tempC': [],
            'windspeedKmph': [],
            'year': [],
            'day': [],
            'hour': [],
            'lat': [],
            'lng': []}

    for i in range(48):
        now = starting_time + timedelta(hours=i)
        w = one_call.forecast_hourly[i]

        data['humidity'].append(w.humidity)
        data['pressure'].append(w.pressure["press"])
        data['tempC'].append(w.temperature("celsius")["temp"])
        data['windspeedKmph'].append(w.wind()["speed"])
        data['year'].append(now.year)
        data['day'].append(now.day)
        data['hour'].append(now.hour)
        data['lat'].append(lat)
        data['lng'].append(lng)

    df = pd.DataFrame(data, columns=['humidity', 'pressure', 'tempC',
                                     'windspeedKmph', 'year', 'day',
                                     'hour', 'lat', 'lng'])

    return df