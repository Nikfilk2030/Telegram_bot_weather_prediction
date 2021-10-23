import first_training_data as first
import predict_weather as predict
import train_model as train
#import weather_history
import cities_latlngs as cll


if __name__ == '__main__':
    cll.create_latlng(cll.get_cities_list('cities.txt'))
    weather_data = first.create_train_data('latlngs.txt')
    train.train_weather_predictor(weather_data)