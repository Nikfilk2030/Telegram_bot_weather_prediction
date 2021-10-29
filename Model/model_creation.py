import first_training_data
import predict_weather
import train_model
from Weather_getter import Get_weather as gw
import weather_history
from Weather_getter import keys


def model_creation():
    # weather_history.get_history_data(3, '28-OCT-2021', '28-OCT-2021', keys.wwo_token,
    #                                 'cities.txt', 'Cities')
    # cll.create_latlng('cities.txt')
    weather_data = first_training_data.create_train_data('Model\\latlngs.txt')
    regressor = train_model.train_weather_predictor(weather_data)
    #print(predict_weather.predict(gw.get_three_days_weather(55.45, 37.36), regressor))

