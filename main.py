import first_training_data as first
import predict_weather as pred
import train_model as train
import weather_history
import cities_latlngs as cll


if __name__ == '__main__':
    #weather_history.get_history_data(3, '18-OCT-2020', '18-OCT-2021', 'eb17522691384ca08f4205244212010', 'cities.txt', 'cities')
    cll.create_latlng('cities.txt')
    weather_data = first.create_train_data('latlngs.txt')
    regressor = train.train_weather_predictor(weather_data)
    print(pred.predict(weather_data, regressor))