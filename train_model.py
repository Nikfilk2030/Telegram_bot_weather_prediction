import pandas as pd
import typing as tp
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


def train_weather_predictor(data: pd.DataFrame, regressor: RandomForestRegressor = None) -> RandomForestRegressor:
    x = data.drop(['tempC'], axis=1)
    y = data['tempC']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=123)
    regressor = regressor if regressor else RandomForestRegressor(n_estimators=30, random_state=123)
    regressor.fit(x_train, y_train)
    print_fitting_result('training', regressor.score(x_train, y_train), regressor.score(x_test, y_test))
    return regressor

def print_fitting_result(fit_mode: str, score_train: float, score_test: float) -> tp.NoReturn:
    print('model was fitted with ' + fit_mode + ' data')
    print('regressor\'s score on training data: ', score_train)
    print('regressor\'s score on testing data: ', score_test, '\n')
