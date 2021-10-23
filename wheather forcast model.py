from wwo_hist import retrieve_hist_data
import pandas as pd
import typing as tp
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime
from geopy.geocoders import Nominatim


def data_formatting(data: pd.DataFrame, latlngs: tp.Dict[str, tp.Tuple[float]]) -> pd.DataFrame:
    data['date_time'] = data['date_time'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
    data['day'] = data['date_time'].apply(lambda x: x.dayofyear)
    data['hour'] = data['date_time'].apply(lambda x: x.hour)
    data['lat'] = data['location'].apply(lambda x: latlngs[x][0])
    data['lng'] = data['location'].apply(lambda x: latlngs[x][1])
    data = data.drop(['date_time', 'location'], axis=1)
    return data

def create_latlng_dict(file: str) -> tp.Dict[str, tp.Tuple]:
    with open(file) as f:
        latlngs = {}
        for x in f.readlines():
            city, lat, lng = x.split()
            latlngs[city] = (float(lat), float(lng),)
    return latlngs

def train_weather_predictor(data: pd.DataFrame, regressor: RandomForestRegressor = None) -> RandomForestRegressor:
    x = data.drop(['tempC'], axis=1)
    y = data['tempC']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=123)
    regressor = regressor if regressor else RandomForestRegressor(n_estimators=12, random_state=0)
    regressor.fit(x_train, y_train)
    print_fitting_result('training', regressor.score(x_train, y_train), regressor.score(x_test, y_test))
    regressor.fit(x_test, y_test)
    print_fitting_result('testing', regressor.score(x_train, y_train), regressor.score(x_test, y_test))
    return regressor

def print_fitting_result(fit_mode: str, score_train: float, score_test: float) -> tp.NoReturn:
    print('model was fitted with ' + fit_mode + ' data')
    print('regressor\'s score on training data: ', score_train)
    print('regressor\'s score on testing data: ', score_test, '\n')

def create_train_data(locations_file: str) -> pd.DataFrame:
    latlngs = create_latlng_dict(locations_file)
    filenames = [city + '.csv' for city in latlngs]
    data = data_formatting(pd.concat([pd.read_csv(file, usecols=[0, 20, 24]) for file in filenames],
                                     ignore_index=True), latlngs)
    for i in data:
        print(i)
    print('your training data')
    print(data)
    return data


weather_data = create_train_data('latlngs.txt')
weather_prediction = train_weather_predictor(weather_data)
