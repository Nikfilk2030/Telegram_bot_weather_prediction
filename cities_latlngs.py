from geopy.geocoders import Nominatim
import typing as tp

def get_latlng(city: str) -> tp.Tuple:
    geolocator = Nominatim(user_agent="weather forecast bot")
    location = geolocator.geocode(city)
    print(location)
    return location.latitude, location.longitude

def create_latlng(cities: tp.List) -> tp.NoReturn:
    with open('latlngs.txt', 'w') as file:
        for city in cities:
            file.write('{} {} {}\n'.format(city, *get_latlng(city)))

def get_cities_list(file: str) -> tp.List:
    with open(file) as f:
        l = [row.strip() for row in f.readlines()]
    return l


create_latlng(get_cities_list('cities.txt'))