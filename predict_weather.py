import pandas as pd
import typing as tp
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


def predict(data: pd.DataFrame, regressor: RandomForestRegressor) -> RandomForestRegressor:
    return regressor.predict(data)


def print_fitting_result(fit_mode: str, score_train: float, score_test: float) -> tp.NoReturn:
    print('model was fitted with ' + fit_mode + ' data')
    print('regressor\'s score on training data: ', score_train)
    print('regressor\'s score on testing data: ', score_test, '\n')
