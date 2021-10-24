import pandas as pd
import typing as tp
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


def predict(data: pd.DataFrame, regressor: RandomForestRegressor) -> np.ndarray:
    x = data.drop(['tempC'], axis=1)
    return regressor.predict(x)


