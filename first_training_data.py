import pandas as pd
import typing as tp
from datetime import datetime
from geopy.geocoders import Nominatim


def data_formatting(data: pd.DataFrame, latlngs: tp.Dict[str, tp.Tuple[float]] = [],
                    location_mode: str='city') -> pd.DataFrame:
    data['date_time'] = data['date_time'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
    data['year'] = data['date_time'].apply(lambda x: x.year)
    data['day'] = data['date_time'].apply(lambda x: x.dayofyear)
    data['hour'] = data['date_time'].apply(lambda x: x.hour)
    data = data.drop(['date_time'], axis=1)
    if location_mode == 'city':
        data['lat'] = data['location'].apply(lambda x: latlngs[x][0])
        data['lng'] = data['location'].apply(lambda x: latlngs[x][1])
        data = data.drop(['location'], axis=1)
    return data

def create_latlng_dict(file: str) -> tp.Dict[str, tp.Tuple]:
    with open(file) as f:
        latlngs = {}
        for x in f.readlines():
            city, lat, lng = x.split()
            latlngs[city] = (float(lat), float(lng),)
    return latlngs

def create_train_data(locations_file: str) -> pd.DataFrame:
    latlngs = create_latlng_dict(locations_file)
    filenames = [city + '.csv' for city in latlngs]
    data = data_formatting(pd.concat([pd.read_csv('cities\\' + file, usecols=[0, 17, 19, 20, 23, 24]) for file in filenames],
                                     ignore_index=True), latlngs)
    for i in data:
        print(i, data[i][0], type(data[i][0]))
    print('your training data')
    print(data)
    return data
